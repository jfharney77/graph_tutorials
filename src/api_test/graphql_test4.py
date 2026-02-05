from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        t_e_m_i(
            s_t: String
        ): EMI
    }

    type EMI {
        t_e_m_o: TEMD
        i_d: String
    }

    type TEMD {
        sT: String
        dHE: String
        dHA: String
        bHA: String
        sHA: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("t_e_m_i")
def resolve_t_e_m_i(obj, info, **kwargs):
    return {
        "t_e_m_o": None,
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

    parser = argparse.ArgumentParser(description="GraphQL TEMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
