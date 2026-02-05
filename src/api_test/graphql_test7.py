from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        o_m_i_info(
            st: String
            sD: String
            eD: String
            vI: String
            fV: String
        ): OMI
    }

    type OMI {
        o_w_o: String
        i_d: String
        vST: String
        w_f: String
        a: [String]
        a_i: [String]
        a_v_t: [String]
        t_v: Int
        t_s: [String]
        v_t: [String]
        l_v: [String]
        v: [String]
        v_v_t: [String]
        d: [String]
        d_i: [String]
        s: [String]
        l: [String]
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
        crm_signals: [CDD]
    }

    type CDD {
        o_c_d: String
        d_s: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("o_m_i_info")
def resolve_o_m_i_info(obj, info, **kwargs):
    return {
        "o_w_o": "",
        "i_d": "",
        "vST": "",
        "w_f": "",
        "a": [],
        "a_i": [],
        "a_v_t": [],
        "t_v": 0,
        "t_s": [],
        "v_t": [],
        "l_v": [],
        "v": [],
        "v_v_t": [],
        "d": [],
        "d_i": [],
        "s": [],
        "l": [],
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
        "crm_signals": []
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
