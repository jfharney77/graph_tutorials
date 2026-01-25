# graph_tutorials

A repository for various neo4j learnings

## From windsurf

Option 1: Using podman-compose (Recommended)

```
podman-compose -f podman-compose.yml up -d
```

Option 2: Using podman directly with the Dockerfile

```
podman build -t neo4j-graph .
podman run -d `
  --name neo4j-graph `
  -p 7474:7474 `
  -p 7687:7687 `
  -e NEO4J_AUTH=neo4j/password `
  neo4j-graph
```

To access Neo4j:

Browser UI: http://localhost:7474
Username: neo4j
Password: password
Bolt Connection: bolt://localhost:7687

Useful podman commands:

```
# Stop the container
podman-compose -f podman-compose.yml down

# View logs
podman-compose -f podman-compose.yml logs -f

# Stop/Start
podman stop neo4j-graph
podman start neo4j-graph


```
