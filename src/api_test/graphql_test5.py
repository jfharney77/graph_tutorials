from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

# Define the GraphQL schema
type_defs = """
    type Query {
        t_a_m_i(
            s_t: String
        ): TAMI
    }

    type TAMI {
        t_a_m_o: TAMD
        i_d: String
        e_m: String
    }

    type TAMD {
        tM: TM
        aA: AA
        aH: AH
    }

    type TM {
        cD: String
        aOH: String
        a: String
        u: String
        aT: String
    }

    type AA {
        cD: String
        dD: [DD]
        eEC: [String]
        fFL: [String]
        pAI: String
        hSD: String
        fAD: String
        iHDUW: String
        iHDU: String
        iHMU: String
        iHCU: String
        iARHU: String
        iMDHU: String
        iADF: String
        iHC: String
        iMC: String
        iLC: String
        iLB: String
        iLS: String
        mTOAV: String
        iB: String
        iWS: String
    }

    type AH {
        cD: String
        nMH: String
        nC: String
        nBH: String
        dS: [DS]
    }

    type AT {
        c: String
        m: String
        a: String
        o: String
    }

    type DD {
        dE: String
        dI: String
        sDIU: String
        rC: String
        dT: String
        dH: String
    }

    type DS {
        dEI: String
        dI: String
        s: String
    }
"""

# Create query resolver
query = QueryType()


@query.field("t_a_m_i")
def resolve_t_a_m_i(obj, info, **kwargs):
    return {
        "t_a_m_o": None,
        "i_d": "",
        "e_m": ""
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

    parser = argparse.ArgumentParser(description="GraphQL TAMI Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.service_port)
