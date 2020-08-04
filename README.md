# pygments-promql

A PromQL lexer for Pygments

# Installation

## Using `pip`

Run:

```console
pip install pygments-promql
```

## From source code

If you wan to test, play or contribute to this repo:

```console
python setup.py install
```

# Usage

```
pygmentize -f png -O "full,style=monokai,line_numbers=False" -o /tmp/example.png tests/example.promql
```
