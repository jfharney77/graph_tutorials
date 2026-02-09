import json
import requests


def query_w_info(variables=None):
    url = "http://localhost:6001/graphql"

    query = """
    query (
        $v_id: String
        $v_dts: String
        $v_dt: String
        $svc_tag_id: String
        $v_p_u_stem: String
        $v_c_c: String
        $s_a_i_v: String
        $s_d_i: String
        $h_s_n: String
        $v_r_i: String
        $o_n: String
        $d_g_c: String
    ) {
        w_info(
            v_id: $v_id
            v_dts: $v_dts
            v_dt: $v_dt
            svc_tag_id: $svc_tag_id
            v_p_u_stem: $v_p_u_stem
            v_c_c: $v_c_c
            s_a_i_v: $s_a_i_v
            s_d_i: $s_d_i
            h_s_n: $h_s_n
            v_r_i: $v_r_i
            o_n: $o_n
            d_g_c: $d_g_c
        ) {
            w_m_o
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
    print("Testing GraphQL w_info service...")

    sample_vars = {
        "v_id": "example-id",
        "svc_tag_id": "svc-123",
        "v_dt": "2026-02-05",
    }

    result = query_w_info(sample_vars)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
