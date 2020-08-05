# -*- coding: utf-8 -*-
"""
    Test and look for unknown tokens using PromQLLexer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2020 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from pygments.lexers import get_lexer_by_name
from pygments.token import Error


def test_unknown_tokens():
    with open("tests/example.promql") as f:
        text = f.read()
    lx = get_lexer_by_name("promql")
    ntext = []
    for token_type, value in lx.get_tokens(text):
        ntext.append(value)
        assert token_type != Error, (
            "lexer %s generated error token: %r at position %d: %s"
            % (lx, value, len(u"".join(ntext)), u"".join(ntext),)
        )
