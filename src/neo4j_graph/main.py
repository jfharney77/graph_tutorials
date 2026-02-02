
from neo4j import GraphDatabase

# Neo4j connection parameters
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

def main():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    try:
        # Test the connection
        with driver.session() as session:
            result = session.run("RETURN 'Neo4j is connected!' as message")
            for record in result:
                print(record["message"])
    finally:
        driver.close()

if __name__ == '__main__':
    main()