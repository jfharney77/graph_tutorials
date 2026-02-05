import json
import requests


def query_c_a_r_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query (
        $sT: String
        $aT: String
        $aI: String
        $aL: Int
        $l: String
    ) {
        c_a_r_m_i(
            sT: $sT
            aT: $aT
            aI: $aI
            aL: $aL
            l: $l
        ) {
            i_d
            c_a_r_m_o {
                a_i
                a_t
                a_s
                a_l_u
                r_a_i
                a_l
            }
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
    print("Testing GraphQL c_a_r_m_i service...")
    sample_vars = {
        "sT": "example",
        "aT": "atype",
        "aI": "aid",
        "aL": 1,
        "l": "en",
    }
    result = query_c_a_r_m_i(sample_vars)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
