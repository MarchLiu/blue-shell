import argparse
import os.path
import sys
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession
from prompt_toolkit import prompt
import readline
import requests
import atexit


def ask(message, args, context=None):
    req = {
        "prompt": message,
        "stream": False,
        "system": args.system,
        "model": args.model
    }
    if context:
        req["context"] = context
    gen_url = os.path.join(args.url, "api/generate")
    resp = requests.post(url=gen_url, json=req, headers={"Content-Type": "application/json"})
    return resp.json()


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
        epilog='Powered By Python')

    parser.add_argument('--url', action="store", default="http://127.0.0.1:11434")  # positional argument
    parser.add_argument('-p', '--prompt',
                        action='store')  # string
    parser.add_argument("-m", "--model", action="store")
    parser.add_argument('-s', '--system',
                        action='store', default="You are a helpful assistant. 你是一个乐于助人的助手。")  # string

    return parser.parse_args()


def runner(args):
    context = None
    session = PromptSession()

    while True:
        try:
            line = session.prompt('ollama: ')

            print(line)
            result = ask(line, args, context)
            context = result.get("context")
            print(result.get("response"))
        except EOFError:
            exit(0)


if __name__ == "__main__":
    args = load_args()
    runner(args)
