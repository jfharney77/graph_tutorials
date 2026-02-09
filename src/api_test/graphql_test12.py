from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        o_m_i(
            sT: String
            sD: String
            eD: String
            vI: String
            fV: String
        ): OI
    }

    type OI {
        o_m_o: String
        i_d: String
        vST: [String]
        w_f: String
        a: [String]
        a_id: [String]
        a_v_t: [String]
        t_v: Int
        t_s: [String]
        v_t: [String]
        l_v: [String]
        v: [String]
        v_v_t: [String]
        dr: [String]
        d_i: [String]
        se: [String]
        lob: [String]
        c_t: [String]
        c_q: [String]
        u_i: [String]
        o_d: [String]
        v_f: [String]
        v_i: [String]
        e_c: [String]
        i_s_t: [String]
        i_e_m: [String]
        p_t: String
        c_sig: [CDD]
    }

    type CDD {
        o_c_d: String
        d_s: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("o_m_i")
def resolve_o_m_i(obj, info, **kwargs):
    return {
        "o_m_o": "",
        "i_d": "",
        "vST": [],
        "w_f": "",
        "a": [],
        "a_id": [],
        "a_v_t": [],
        "t_v": 0,
        "t_s": [],
        "v_t": [],
        "l_v": [],
        "v": [],
        "v_v_t": [],
        "dr": [],
        "d_i": [],
        "se": [],
        "lob": [],
        "c_t": [],
        "c_q": [],
        "u_i": [],
        "o_d": [],
        "v_f": [],
        "v_i": [],
        "e_c": [],
        "i_s_t": [],
        "i_e_m": [],
        "p_t": "",
        "c_sig": []
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

    parser = argparse.ArgumentParser(description="GraphQL OMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
