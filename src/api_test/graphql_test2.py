from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        w_info(
            v_id: String
            v_dts: String
            v_dt: String
            svc_tag_id: String
            v_p_u_stem: String
            v_c_c: String
            s_a_i_v: String
            s_d_i: String
            h_s_n: String
            v_r_i: String
            o_n: String
            d_g_c: String
        ): WItem
    }

    type WItem {
        w_m_o: Int
        i_d: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("w_info")
def resolve_w_info(obj, info, **kwargs):
    return {
        "w_m_o": 0,
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

    parser = argparse.ArgumentParser(description="GraphQL WInfo Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
