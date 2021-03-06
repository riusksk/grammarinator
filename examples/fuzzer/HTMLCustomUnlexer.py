# Copyright (c) 2017 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

from HTMLUnlexer import HTMLUnlexer

from grammarinator.runtime import *


class HTMLCustomUnlexer(HTMLUnlexer):

    def __init__(self, *, max_depth=float('inf')):
        super(HTMLCustomUnlexer, self).__init__(max_depth=max_depth)

    # You probably want to rewrite this with a distinct CSS fuzzer.
    def style_sheet(self):
        return UnlexerRule(src='* {' \
                                '  background: green;' \
                                '}')
