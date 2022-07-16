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
    help_msg = """
Rust Playground Locally allows you to play around rust code without the need to create a rust file and compile it.
At its core, this program submits your Rust code to the Rust playground API (https://play.rust-lang.org/) which executes your
Rust code and prints out the stdout or stderr (if any).

You can directly write Rust code in the terminal using this command:
`python3 -m rust_playground`
"""
    if len(argv) > 1 and (argv[1] == "-h" or argv[1] == "--help"):
        print(help_msg)
        return

    welcome_prompt = '''Welcome to Rust Playground Locally!
Your Rust Code will be sent to the Rust Playground (https://play.rust-lang.org/) API so please make sure you have an internet connection.'''
    print(welcome_prompt)

    lines = []
    while True:
        raw_input = input('>>> ')
        if not raw_input:
            break
        lines.append(raw_input + '\n')
    raw_code_input = ''.join(lines).strip()

    print('\nRunning your code, please wait...\n')

    run_rust_code(raw_code_input)

if __name__ == '__main__':
    main()

