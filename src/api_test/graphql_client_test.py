import requests
import json


def query_persona_model(s_param=None):
    url = "http://localhost:8000/graphql"
    
    # GraphQL query
    query = """
    query ($s: String) {
        p_model_info(s: $s) {
            persona_model_output {
                p_type
                user_type
            }
            is_default
        }
    }
    """
    
    # Payload with query and variables
    payload = {
        "query": query,
        "variables": {
            "s": s_param
        }
    }
    
    # Send POST request
    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    return response.json()


def main():
    # Example usage
    print("Testing GraphQL persona service...")
    
    # Test with a parameter
    result = query_persona_model("test_string")
    print("\nResult with parameter 's=test_string':")
    print(json.dumps(result, indent=2))
    
    # Test without parameter
    result2 = query_persona_model()
    print("\nResult without parameter:")
    print(json.dumps(result2, indent=2))


if __name__ == '__main__':
    main()
