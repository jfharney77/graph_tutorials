from neo4j import GraphDatabase
from datetime import datetime, timezone

# Neo4j connection parameters
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"
NEO4J_DATABASE = "neo4j"

def query_person_nodes(driver):
    """Query all nodes with the label 'Person' and return only the 'from' property"""
    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run("MATCH (p:Person) RETURN p.from")
        
        people = []
        for record in result:
            people.append(record["p.from"])
        
        return people


def create_product_nodes(driver, product_names: list[str]) -> None:
    """Create `Product` nodes with a `name` property for each name in `product_names`.

    Existing product nodes with the same `name` are not duplicated (uses MERGE).
    """
    if not product_names:
        return

    cypher = """
    UNWIND $names AS name
    MERGE (p:Product {name: name})
    """

    with driver.session(database=NEO4J_DATABASE) as session:
        session.run(cypher, names=product_names)

def create_connected_product_and_links(driver, connected_product: str, product_names: list[str]) -> None:
    """Ensure `connected_product` exists as a `Product` node, create any missing
    product nodes from `product_names`, and create bidirectional
    `:CompatibleWith` relationships between the connected product and each
    product in `product_names`.

    Relationship property `creation_time` is set only when the relationship is
    created (uses `ON CREATE SET`).
    """
    if not connected_product:
        return

    timestamp = datetime.now(timezone.utc).isoformat()

    cypher = """
    MERGE (c:Product {name: $connected})
    WITH c

    UNWIND $names AS pname
    WITH c, trim(pname) AS pname WHERE pname IS NOT NULL AND pname <> "" AND pname <> $connected
    MERGE (p:Product {name: pname})

    MERGE (c)-[r:CompatibleWith]->(p)
    ON CREATE SET r.creation_time = $ts

    MERGE (p)-[r2:CompatibleWith]->(c)
    ON CREATE SET r2.creation_time = $ts
    """

    with driver.session(database=NEO4J_DATABASE) as session:
        session.run(cypher, connected=connected_product, names=product_names, ts=timestamp)
def main():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    try:
        # Query all Person nodes
        persons = query_person_nodes(driver)
        
        if persons:
            print(f"Found {len(persons)} Person node(s) with 'from' property:")
            for person in persons:
                print(f"  - {person}")
        else:
            print("No Person nodes found in the graph.")
    finally:
        driver.close()

if __name__ == '__main__':
    main()
