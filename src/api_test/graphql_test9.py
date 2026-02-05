from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    input ITD {
        i: String
        s: Float
    }

    input ADD {
        aI: String
        iT: [ITD]
        uD: String
        vD: String
    }

    input VDD {
        vI: String
        iT: [ITD]
        uDT: String
        vD: String
    }

    type Query {
        i_t_p_m_i(
            sT: String
            aD: [ADD]
            vD: [VDD]
        ): ITPMI
    }

    type ITPMI {
        i_d: String
        i_t_m_o: ITPD
    }

    type ITPD {
        i_t: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("i_t_p_m_i")
def resolve_i_t_p_m_i(obj, info, **kwargs):
    return {
        "i_d": "",
        "i_t_m_o": {
            "i_t": ""
        }
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

    parser = argparse.ArgumentParser(description="GraphQL ITPMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
