from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        o_i_m_i(
            vI: String
        ): OIMI
    }

    type OIMI {
        i_d: String
        o_i_m_o: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("o_i_m_i")
def resolve_o_i_m_i(obj, info, **kwargs):
    return {
        "i_d": "",
        "o_i_m_o": ""
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

    parser = argparse.ArgumentParser(description="GraphQL OIMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
