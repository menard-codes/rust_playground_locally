# Rust Playground Locally

## Abstract

**Rust Playground Locally** is a simple program that allows you to play around rust code in your local machine without creating a new file and compiling it. This is heavily insprired by
REPL environmets that are common among interpreted languages like Python and Ruby. In a sense, **Rust Playground Locally** is a *REPL-like* environment
for Rust.

This simple program uses the Rust code execution API in [Rust Playground](https://play.rust-lang.org/) to execute the rust code. That said, **make sure you have an internet connection
when using this.**

## Prerequisites

Since it's written in Python:

- [Python3](https://www.python.org/downloads/)
- [Requests - A python library](https://pypi.org/project/requests/)

## Getting Started

To get started, clone this repo and write a simple hello world program in Rust.

1. Clone this repo:

```sh
git clone git@github.com:menard-codes/rust_playground_locally.git
```

2. Install dependencies

```sh
cd rust_playground_locally
pip3 install requirements.txt # or pip3 install -r requirements.txt
```

3. Run the rust playground (make sure you're within its directory)

```sh
python3 -m rust_playground
```

<SS HERE>

4. Write a simple hello world program and execute it. Again, if things went right through, you should see something like this:
  
 <HELLO WORLD HERE>
 
