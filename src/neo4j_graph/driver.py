from neo4j import GraphDatabase

from scraper import url_scraper, find_compatibility2
from first import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE, create_product_nodes, create_connected_product_and_links

from neo4j import GraphDatabase
from first import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
#from src.driver import clear_database

URL = "https://www.dell.com/en-us/shop/dell-2tb-performance-ssd-tlc-2280-gen3/apd/ab400209/storage-drives-media#compatibility_section"


def run_scrape_and_create(driver, connected_product: str, url: str) -> None:
    """Scrape `url`, extract compatibility products, and create product nodes
    and relationships in the provided Neo4j `driver`.

    Args:
        driver: An open Neo4j driver instance.
        connected_product: The main product name to connect others to.
        url: The page URL to scrape.
    """
    # 1) Scrape the page
    html = url_scraper(url)

    # 2) Extract compatibility product strings
    products = find_compatibility2(html)
    print(f"Found {len(products)} compatibility items")
    for p in products:
        print(f"  - {p}")

    if not products:
        print("No products to insert into Neo4j.")
        return

    # 3) Insert into Neo4j and create compatibility relationships
    create_connected_product_and_links(driver, connected_product, products)


def clear_database(driver) -> None:
    """Remove all nodes and relationships from the connected Neo4j database.

    This runs `MATCH (n) DETACH DELETE n` against the database referenced by
    `NEO4J_DATABASE`.
    """
    cypher = "MATCH (n) DETACH DELETE n"
    with driver.session(database=NEO4J_DATABASE) as session:
        session.run(cypher)


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        connected_product = "Dell 2TB Performance SSD TLC 2280 Gen3"
        run_scrape_and_create(driver, connected_product, URL)
        print("Product nodes and CompatibleWith relationships created/merged into Neo4j.")
    finally:
        driver.close()


def main_clear():

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        clear_database(driver)
    finally:
        driver.close()

if __name__ == "__main__":
    #main_clear()
    main()