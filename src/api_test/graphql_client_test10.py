import json
import requests


def query_i_a_r_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query (
        $a_i: String
        $p_c: String
        $l: String
        $a_l: String
        $v_i: String
        $s_p: String
    ) {
        i_a_r_m_i(
            a_i: $a_i
            p_c: $p_c
            l: $l
            a_l: $a_l
            v_i: $v_i
            s_p: $s_p
        ) {
            i_d
            e_m
            i_a_r_m_o {
                a_i
                a_t
                a_s
                u_d
                r_a_i
                l
                f_e
                tcd
                e
                c1
                c2
                ld
                g_p
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
    print("Testing GraphQL i_a_r_m_i service...")
    sample_vars = {
        "a_i": "a1",
        "p_c": "pc",
        "l": "en",
        "a_l": "1",
        "v_i": "vi",
        "s_p": "sp",
    }
    result = query_i_a_r_m_i(sample_vars)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
