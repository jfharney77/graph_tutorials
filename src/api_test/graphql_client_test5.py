import json
import requests


def query_t_a_m_i(variables=None):
    url = "http://localhost:8000/graphql"

    query = """
    query ($s_t: String) {
        t_a_m_i(s_t: $s_t) {
            t_a_m_o {
                tM {
                    cD
                    aOH
                    a
                    u
                    aT
                }
                aA {
                    cD
                    dD { dE dI sDIU rC dT dH }
                    eEC
                    fFL
                    pAI
                    hSD
                    fAD
                    iHDUW
                    iHDU
                    iHMU
                    iHCU
                    iARHU
                    iMDHU
                    iADF
                    iHC
                    iMC
                    iLC
                    iLB
                    iLS
                    mTOAV
                    iB
                    iWS
                }
                aH {
                    cD
                    nMH
                    nC
                    nBH
                    dS { dEI dI s }
                }
            }
            i_d
            e_m
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
    print("Testing GraphQL t_a_m_i service...")
    result = query_t_a_m_i({"s_t": "example"})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
