import json
import requests


def query_i_t_p_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query ($sT: String, $aD: [ADD], $vD: [VDD]) {
        i_t_p_m_i(sT: $sT, aD: $aD, vD: $vD) {
            i_d
            i_t_m_o { i_t }
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
    print("Testing GraphQL i_t_p_m_i service...")
    sample_vars = {
        "sT": "example",
        "aD": [{"aI": "a1", "iT": [{"i": "x", "s": 1.0}]}],
        "vD": [{"vI": "v1", "iT": [{"i": "y", "s": 2.0}]}],
    }
    result = query_i_t_p_m_i(sample_vars)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
