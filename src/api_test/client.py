import requests


def call_echo_endpoint(echo_text: str):
    url = "http://localhost:6001/"
    payload = {"echostring": echo_text}
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    return response.json()


def main():
    # Example usage
    result = call_echo_endpoint("worlddd")
    print(result)


if __name__ == '__main__':
    main()
