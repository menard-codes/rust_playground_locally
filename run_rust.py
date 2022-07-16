from sys import argv
import requests
import json

def run_rust_code(code: str) -> None:
    URL = "https://play.rust-lang.org/evaluate.json"
    payload = {
        "version": "stable",
        "optimize": "0",
        "code": code,
        "edition": "2015"
    }
    data = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    response = requests.post(url=URL, data=data, headers=headers)
    print(response.json()["result"])

def main():
    code_input = argv[1]
    run_rust_code(code_input)

if __name__ == '__main__':
    main()

