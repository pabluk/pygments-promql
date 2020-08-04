# pygments-promql

![Python package](https://github.com/pabluk/pygments-promql/workflows/Python%20package/badge.svg)

A PromQL lexer for [Pygments](https://pygments.org/).


# Installation

## Using pip

Run:

```console
pip install pygments-promql
```

## From source code

or after cloning this repo:

```console
python setup.py install
```

# Usage

## Command-line

Showing colorized output in a terminal:

```console
pygmentize tests/example.promql
```

Or to generate a PNG file:

```console
pygmentize -f png -O "line_numbers=False,style=monokai" -o example.png tests/example.promql
```
![PromQL syntax highlighted](https://raw.githubusercontent.com/pabluk/pygments-promql/master/tests/example.png)

## Python code

The following example:

```python
from pygments import highlight
from pygments.formatters import HtmlFormatter
from promql import PromQLLexer

query = 'http_requests_total{handler="/api/comments"}'
print(highlight(query, PromQLLexer(), HtmlFormatter()))
```

will generate this HTML output:

```html
<div class="highlight">
    <pre>
        <span></span>
	<span class="nv">http_requests_total</span>
	<span class="p">{</span>
	<span class="nl">handler</span>
	<span class="o">=</span>
	<span class="s">&quot;/api/comments&quot;</span>
	<span class="p">}</span>
	<span class="w"></span>
    </pre>
</div>
```

Use `HtmlFormatter(noclasses=True)` to include CSS inline styles on every `<span>` tag.


# Testing

If you wan to test, play or contribute to this repo:

```console
pip install -r requirements.txt
pip install -e .
pytest -v
```
