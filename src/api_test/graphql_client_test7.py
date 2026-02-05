import json
import requests


def query_o_m_i_info(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query (
        $st: String
        $sD: String
        $eD: String
        $vI: String
        $fV: String
    ) {
        o_m_i_info(
            st: $st
            sD: $sD
            eD: $eD
            vI: $vI
            fV: $fV
        ) {
            o_w_o
            i_d
            vST
            w_f
            a
            a_i
            a_v_t
            t_v
            t_s
            v_t
            l_v
            v
            v_v_t
            d
            d_i
            s
            l
            c_t
            c_q
            u_i
            o_d
            v_f
            v_i
            e_c
            i_s_t
            i_e_m
            p_t
            crm_signals { o_c_d d_s }
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
    print("Testing GraphQL o_m_i_info service...")
    sample_vars = {
        "st": "example",
        "sD": "2026-02-05",
        "eD": "2026-02-06",
        "vI": "vid",
        "fV": "fval",
    }
    result = query_o_m_i_info(sample_vars)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
