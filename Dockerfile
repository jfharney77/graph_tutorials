FROM neo4j:latest

# Set environment variables for Neo4j
ENV NEO4J_AUTH=neo4j/password
ENV NEO4J_PLUGINS=apoc

EXPOSE 7474 7687
