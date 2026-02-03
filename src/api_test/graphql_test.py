from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema, graphql_sync
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        p_model_info(s: String): PModelItem
    }

    type POutputItem {
        p_type: String
        user_type: String
    }

    type PModelItem {
        persona_model_output: [POutputItem]
        is_default: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("p_model_info")
def resolve_p_model_info(obj, info, s=None):
    return {
        "persona_model_output": [],
        "is_default": "True"
    }


# Create executable schema
schema = make_executable_schema(type_defs, query)

# Create FastAPI app
app = FastAPI()

# Mount GraphQL endpoint
app.mount("/graphql", GraphQL(schema, debug=True))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
