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

```console
pygmentize -f png -O "line_numbers=False" -o tests/example.png tests/example.promql
```
![promql](tests/example.png)
