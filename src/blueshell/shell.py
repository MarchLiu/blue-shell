import argparse
import atexit
import json
import os.path
import pprint
import sys

import readline
import requests
import rich.markdown
from prompt_toolkit import PromptSession
from rich.console import Console


def ask(message, args, context=None):
    req = {
        "prompt": message,
        "stream": True,
        "system": args.system,
        "model": args.model
    }
    if context:
        req["context"] = context
    if args.format == "json":
        req["format"] = "json"

    gen_url = os.path.join(args.url, "api/generate")

    with (requests.Session() as session,
          session.post(gen_url, json=req, headers={"Content-Type": "application/json"}) as resp):
        for token in resp.iter_lines():
            yield json.loads(token)

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)


def load_args():
    histfile = os.path.join(os.path.expanduser("~"), ".blueshell_history")
    try:
        readline.read_history_file(histfile)
        h_len = readline.get_current_history_length()
    except FileNotFoundError:
        open(histfile, 'wb').close()
        h_len = 0
    atexit.register(save, h_len, histfile)

    parser = argparse.ArgumentParser(
        prog='Blue Shell',
        description='A AI assistant for local ai service',
        epilog='Powered By Python, Rich, prompt_toolkit and requests')

    parser.add_argument('--url', action="store", default="http://127.0.0.1:11434")  # positional argument
    parser.add_argument('-p', '--prompt',
                        action='store')  # string
    parser.add_argument("-m", "--model", action="store")
    parser.add_argument("-f", "--format", action="store",
                        default="plain", choices=["markdown", "plain", "json"])
    parser.add_argument('-s', '--system',
                        action='store', default="You are a helpful assistant. 你是一个乐于助人的助手。")  # string

    return parser.parse_args()


def output(response, args):
    ty = type(response)
    if ty is str:
        content = response
    elif (ty is tuple) or (ty is list):
        content = "\n".join(response)
    else:
        content = str(response)

    console = Console()
    if args.format == "markdown":
        md = rich.markdown.Markdown(content)
        console.print(md)
    elif args.format == "json":
        try:
            j = json.loads(content)
        except Exception:
            print(content)
        else:
            md = rich.markdown.Markdown('```json\n' + json.dumps(j, indent=2)+ '\n```')
            console.print(md)
    else:
        print(content)

def runner(args):

    context = None
    session = PromptSession()

    while True:
        try:
            line = session.prompt(f'(ollama {args.model})# ')
            print()
            content = ""
            for j in ask(line, args, context):
                if j["done"]:
                    context = j["context"]
                response = j.get("response")
                if args.format == "plain":
                    sys.stdout.write(response)
                else:
                    content += response

            if args.format == "plain":
                print()
            else:
                output(content, args)

        except KeyboardInterrupt:
            print("Control-c")
        except EOFError:
            exit(0)


if __name__ == "__main__":
    args = load_args()
    runner(args)
