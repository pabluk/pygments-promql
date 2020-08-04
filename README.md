# pygments-promql

A PromQL lexer for [Pygments](https://pygments.org/).

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

Showing colorized output in a console:

```console
$ pygmentize tests/example.promql
# Example query
go_gc_duration_seconds{instance="localhost:9090",job="alertmanager"} + absent_over_time(scrape_duration_seconds[4m]) # A single line comment
```

Or to generate a PNG file:

```console
pygmentize -f png -O "line_numbers=False" -o tests/example.png tests/example.promql
```
![promql](tests/example.png)
