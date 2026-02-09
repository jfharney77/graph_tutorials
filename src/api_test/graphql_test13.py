from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        p_m_i(
            st: String
        ): PMI
    }

    type PMI {
        p_m_o: [POI]
        i_d: String
    }

    type POI {
        p_t: String
        u_t: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("p_m_i")
def resolve_p_m_i(obj, info, **kwargs):
    return {
        "p_m_o": [],
        "i_d": ""
    }


# Create executable schema
schema = make_executable_schema(type_defs, query)

# Create FastAPI app
app = FastAPI()

# Mount GraphQL endpoint
app.mount("/graphql", GraphQL(schema, debug=True))


if __name__ == "__main__":
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser(description="GraphQL PMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
