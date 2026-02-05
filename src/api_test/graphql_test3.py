from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        v_r_m_i(
            rPV: String!
            language: String
            accessLevel: Int
            pVV: [VDD]
        ): VRMI
    }

    type VRMI {
        v_r_m_o: [VRMD]
        i_d: String
    }

    type VRMD {
        rPV: [String]
        sL: [String]
        vI: String
        l: String
        du: String
        im: String
        mD: String
        vU: String
        vT: String
        t: String
        vTy: String
        de: String
        aL: String
        pS: String
        dDT: String
        expDT: String
        v_c: String
    }

    input VDD {
        v: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("v_r_m_i")
def resolve_v_r_m_i(obj, info, **kwargs):
    return {
        "v_r_m_o": [],
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

    parser = argparse.ArgumentParser(description="GraphQL VRMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
