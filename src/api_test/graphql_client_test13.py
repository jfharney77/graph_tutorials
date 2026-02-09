import json
import requests


def query_p_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query ($st: String) {
        p_m_i(st: $st) {
            p_m_o {
                p_t
                u_t
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
    print("Testing GraphQL p_m_i service...")
    result = query_p_m_i({"st": "example"})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
