# Blue Shell

Blue Shell is a AI Chat Shell for local service. 0.0.1 version support ollama

## Installation

```
pip install blueshell
```

## Usage

At simplest, run 

```shell
python -m blueshell.shell -m "codellama" 
```

If ollama isn't listening default port, for example 11435. we could pass a url parameter like this:

```shell
python -m blueshell.shell -m "codellama" --url http://127.0.0.1:11435
```

More options could run help:

```shell
$ python -m blueshell.shell --help
usage: Blue Shell [-h] [--url URL] [-p PROMPT] [-m MODEL]
                  [-f {markdown,plain,json}] [-s SYSTEM]

A AI assistant for local ai service

options:
  -h, --help            show this help message and exit
  --url URL
  -p PROMPT, --prompt PROMPT
  -m MODEL, --model MODEL
  -f {markdown,plain,json}, --format {markdown,plain,json}
  -s SYSTEM, --system SYSTEM

Powered By Python

```

You can list all models in ollama:

```shell
$ python -m blueshell.list
```

List has a option is url:

```shell
$ python -m blueshell.list --url http://127.0.0.1:11435
```


## What's New

### 0.0.1

support ollama

### 0.0.2

document typo

### 0.0.3

print feedback as markdown

### 0.0.4

fixed dependencies miss

### 0.0.5

- add list command
- add format argument
- C-c interrupt repl and continue
- Improved User Experience

### 0.0.6

support json format pretty