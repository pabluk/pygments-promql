# -*- coding: utf-8 -*-
"""
    Basic PromQLLexer Test
    ~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2020 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest

from pygments.token import Token
from promql import PromQLLexer


@pytest.fixture(scope="module")
def lexer():
    yield PromQLLexer()


def test_metric(lexer):
    fragment = u"go_gc_duration_seconds"
    tokens = [
        (Token.Name.Variable, "go_gc_duration_seconds"),
        (Token.Text.Whitespace, "\n"),
    ]
    assert list(lexer.get_tokens(fragment)) == tokens


def test_metric_one_label(lexer):
    fragment = u'go_gc_duration_seconds{instance="localhost:9090"}'
    tokens = [
        (Token.Name.Variable, "go_gc_duration_seconds"),
        (Token.Punctuation, "{"),
        (Token.Name.Label, "instance"),
        (Token.Operator, "="),
        (Token.Literal.String, '"localhost:9090"'),
        (Token.Punctuation, "}"),
        (Token.Text.Whitespace, "\n"),
    ]
    assert list(lexer.get_tokens(fragment)) == tokens


def test_metric_multiple_labels(lexer):
    fragment = u'go_gc_duration_seconds{instance="localhost:9090",job="alertmanager"}'
    tokens = [
        (Token.Name.Variable, "go_gc_duration_seconds"),
        (Token.Punctuation, "{"),
        (Token.Name.Label, "instance"),
        (Token.Operator, "="),
        (Token.Literal.String, '"localhost:9090"'),
        (Token.Punctuation, ","),
        (Token.Name.Label, "job"),
        (Token.Operator, "="),
        (Token.Literal.String, '"alertmanager"'),
        (Token.Punctuation, "}"),
        (Token.Text.Whitespace, "\n"),
    ]
    assert list(lexer.get_tokens(fragment)) == tokens


def test_expression_and_comment(lexer):
    fragment = u'go_gc_duration_seconds{instance="localhost:9090"} # single comment\n'
    tokens = [
        (Token.Name.Variable, "go_gc_duration_seconds"),
        (Token.Punctuation, "{"),
        (Token.Name.Label, "instance"),
        (Token.Operator, "="),
        (Token.Literal.String, '"localhost:9090"'),
        (Token.Punctuation, "}"),
        (Token.Text.Whitespace, " "),
        (Token.Comment.Single, "# single comment"),
        (Token.Text.Whitespace, "\n"),
    ]
    assert list(lexer.get_tokens(fragment)) == tokens
