# -*- coding: utf-8 -*-
"""
    pygments.lexers.promql
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for Prometheus Query Language.

    :copyright: Copyright 2006-2020 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups, default, words
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Whitespace,
)

__all__ = ["PromQLLexer"]


class PromQLLexer(RegexLexer):
    """
    For `PromQL <https://prometheus.io/docs/prometheus/latest/querying/basics/>`_ queries.

    See https://github.com/prometheus/prometheus/tree/master/promql/parser for details about the grammar.
    """

    name = "PromQL"
    aliases = ["promql"]
    filenames = ["*.promql"]

    aggregator_keywords = (
        words(
            (
                "sum",
                "min",
                "max",
                "avg",
                "group",
                "stddev",
                "stdvar",
                "count",
                "count_values",
                "bottomk",
                "topk",
                "quantile",
            ),
            suffix=r"\b",
        ),
        Keyword,
    )

    tokens = {
        "root": [
            (r"\n", Whitespace),
            (r"\s+", Whitespace),
            (r"//.*?\n", Comment.Single),
            # Keywords
            aggregator_keywords,
            # function_keywords,
            # Numbers
            (r"-?[0-9]+\.[0-9]+", Number.Float),
            (r"-?[0-9]+", Number.Integer),
            (r"\(", Operator, "function"),
            (r"\)", Operator),
            (r"{", Punctuation, "labels"),
            (r"\[", Punctuation, "range"),
            (r"#.*?$", Comment.Single),
            (r"(\+|\-|\*|\/|\%|\^)", Operator),
            (r"==|!=|>=|<=|<|>", Operator),
            (r"and|or|unless", Operator.Word),
            (r"(by|without|offset|on|ignoring|group_left|group_right|bool)\b", Keyword),
            (r"[_a-zA-Z][_a-zA-Z0-9]+", Name.Variable),
        ],
        "labels": [
            (r"}", Punctuation, "#pop"),
            (r",", Punctuation),
            (
                r'([_a-zA-Z][_a-zA-Z0-9]*?)(\s*?)(=|!=|=~|~!)(\s*?)(".*?")',
                bygroups(Name.Label, Whitespace, Operator, Whitespace, String),
            ),
        ],
        "range": [
            (r"\]", Punctuation, "#pop"),
            (r"([1-9][0-9]*?)(s|m|h|d|w|y)", bygroups(String, String)),
        ],
        "function": [
            (r"\)", Operator, "#pop"),
            (r"\(", Operator, "#push"),
            default("#pop"),
        ],
    }
