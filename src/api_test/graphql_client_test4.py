import json
import requests


def query_t_e_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query ($s_t: String) {
        t_e_m_i(s_t: $s_t) {
            t_e_m_o {
                sT
                dHE
                dHA
                bHA
                sHA
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
    print("Testing GraphQL t_e_m_i service...")
    result = query_t_e_m_i({"s_t": "example"})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
