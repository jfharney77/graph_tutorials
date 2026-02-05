import json
import requests


def query_o_i_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query ($vI: String) {
        o_i_m_i(vI: $vI) {
            i_d
            o_i_m_o
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
    print("Testing GraphQL o_i_m_i service...")
    result = query_o_i_m_i({"vI": "example"})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
