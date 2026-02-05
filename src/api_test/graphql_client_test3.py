import json
import requests


def query_v_r_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query (
        $rPV: String!
        $language: String
        $accessLevel: Int
        $pVV: [VDD]
    ) {
        v_r_m_i(
            rPV: $rPV
            language: $language
            accessLevel: $accessLevel
            pVV: $pVV
        ) {
            v_r_m_o {
                rPV
                sL
                vI
                l
                du
                im
                mD
                vU
                vT
                t
                vTy
                de
                aL
                pS
                dDT
                expDT
                v_c
            }
            i_d
        }
    }
    """

    payload = {
        "query": query,
        "variables": variables or {},
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


def main():
    print("Testing GraphQL v_r_m_i service...")
    sample_vars = {
        "rPV": "example",
        "language": "en",
        "accessLevel": 1,
        "pVV": [{"v": "value"}],
    }
    result = query_v_r_m_i(sample_vars)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
