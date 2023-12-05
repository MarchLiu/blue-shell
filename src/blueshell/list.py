import argparse
import os.path

import requests


def ask(args):
    get_url = os.path.join(args.url, "api/tags")
    resp = requests.get(url=get_url, headers={"Content-Type": "application/json"})
    for m in resp.json()["models"]:
        yield m["name"]


def load_args():
    parser = argparse.ArgumentParser(
        prog='Blue Shell',
        description='A AI assistant for local ai service',
        epilog='Powered By Python')

    parser.add_argument('--url', action="store", default="http://127.0.0.1:11434")  # positional argument
    return parser.parse_args()


def runner(args):
    for m in ask(args):
        print(m)


if __name__ == "__main__":
    args = load_args()
    runner(args)
