#!/usr/bin/python3

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_promql import PromQLLexer


def main():
    query = 'http_requests_total{handler="/api/comments"}'
    assert 'class="highlight"' in highlight(query, PromQLLexer(), HtmlFormatter())


if __name__ == "__main__":
    main()
