# Blue Shell

Blue Shell is a AI Chat Shell for local service. 0.0.1 version support ollama

## Installation

```
pip install blue-shell
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
python -m blueshell.shell --help
```

## What's New

### 0.1.1

support ollama
