# pygments-promql

[![Python package](https://github.com/pabluk/pygments-promql/workflows/Python%20package/badge.svg)](https://github.com/pabluk/pygments-promql/actions)
[![PyPI](https://img.shields.io/pypi/v/pygments-promql)](https://pypi.org/project/pygments-promql/)
[![PyPI - License](https://img.shields.io/pypi/l/pygments-promql)](https://raw.githubusercontent.com/pabluk/pygments-promql/master/LICENSE)

A PromQL lexer for Pygments.

This Python package provides a [Pygments](https://pygments.org/) lexer for the [Prometheus Query Language](https://prometheus.io/docs/prometheus/latest/querying/basics/). It allows Pygments and other tools ([Sphinx](https://sphinx-doc.org/), [Chroma](https://github.com/alecthomas/chroma), etc) to highlight PromQL queries.

![PromQL syntax highlighted](https://raw.githubusercontent.com/pabluk/pygments-promql/master/tests/example.png)

# Installation

## Using pip

To get the latest version from pypi.org:

```console
pip install pygments-promql
```

# Usage

## Command-line

In a terminal you can echo and pipe a query directly from stdin:

```console
echo 'prometheus_http_requests_total{code="200"}' | pygmentize -l promql
```

Or use a file, for example, create the `example.promql` file with queries from
[tests/example.promql](https://github.com/pabluk/pygments-promql/blob/master/tests/example.promql).
In this case the option `-l promql` is not needed because the lexer will be
detected based on the file extension.

Showing colorized output in a terminal:

```console
pygmentize example.promql
```

To generate a PNG file:

```console
pygmentize -f png -O "line_numbers=False,style=monokai" -o example.png example.promql
```

## Python code

The following example:

```python
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_promql import PromQLLexer

query = 'http_requests_total{handler="/api/comments"}'
print(highlight(query, PromQLLexer(), HtmlFormatter()))
```

Will generate this HTML output:

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

## Sphinx

In order to highlight PromQL syntax in your [Sphinx documentation site](https://www.sphinx-doc.org/en/1.8/index.html)
you just need to add this 3 lines of Python code at the end of your site's `conf.py` file:

```python
from sphinx.highlighting import lexers
from pygments_promql import PromQLLexer
lexers['promql'] = PromQLLexer()
```

Then you will be able to use it like this:

```rst
Here's a PromQL example:

.. code-block:: promql

	# A metric with label filtering
	go_gc_duration_seconds{instance="localhost:9090"}

```

# Testing

If you want to test, play or contribute to this repo:

```console
git clone https://github.com/pabluk/pygments-promql.git
cd pygments-promql/
pip install -r requirements.txt
pip install -e .
pytest -v
```
