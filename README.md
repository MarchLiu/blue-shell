# PyParsec

PyParsec is a Haskell combinator library, PyParsec is a parsec library for python 3+

## Installation

```
pip install pyparsec 
```

## Usage

Just like this:

```
>>> from parsec.state import BasicState
>>> from parsec.combinator import many
>>> from parsec.atom import eq
>>> simple = "It is a simple string."
>>> st = BasicState(simple)
>>> p = eq("I").many
>>> p(st)
['I']
```

## What's New

### 0.6.1

 - add built in combinators decorator
 - add ahead

### 0.7.0

 - add result class

### 0.7.2

 - document

### 0.7.3
 - documents
 - fixed bugs builtin combinators


### 0.7.4
 - uniform result status checker

### 0.7.5
 - typo

### 0.7.6
 - fixed bug in ahead

### 0.8.0
 - uniform functions as python style

### 0.8.1 ~ 0.8.4
- uniform functions as python style
- fixed buildin methods name
- add sep_xxx methods to builtin

### 0.8.5

fixed bug in skip parser