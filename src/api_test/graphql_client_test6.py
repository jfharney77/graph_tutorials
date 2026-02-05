import json
import requests


def query_p_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query ($vI: String) {
        p_m_i(vI: $vI) {
            p_m_o {
                p_f
                s_t
                w_s
            }
            e_m
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
    print("Testing GraphQL p_m_i service...")
    result = query_p_m_i({"vI": "example"})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
