from sys import argv
import requests
import json

def run_rust_code(code: str) -> None:
    URL = "https://play.rust-lang.org/execute"
    payload = {
        "channel": "stable",
        "mode": "debug",
        "edition": "2021",
        "crateType": "bin",
        "tests": False,
        "code": code,
        "backtrace": False
    }
    data = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    response = requests.post(url=URL, data=data, headers=headers)
    print(response.json()["stdout"])

def main():
    code_input = argv[1]
    run_rust_code(code_input)

if __name__ == '__main__':
    main()

