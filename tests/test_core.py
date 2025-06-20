import pytest

from aar_doc.core import _htmlify_code

# Inline user-defined mem limits for IP config values. Example:
# ```yaml
# 192.0.2.1: 256
# 192.0.2.2: 128
# 192.0.2.0-192.0.2.255: 256
# 192.0.2.0/24: 128


# # global mem limit rate
# "0.0.0.0/32": 64
# ```
# User-defined mem limit per IP.\n```yaml\n192.0.2.1: 256\n192.0.2.2: 128\n192.0.2.0-192.0.2.255: 256\n192.0.2.0/24: 128\n\n\n# global mem limit rate\n"0.0.0.0/32": 64\n```\n
@pytest.mark.parametrize(
    ("text", "want"),
    [
        # (
        #     "just a normal text",
        #     "just a normal text",
        # ),
        # (
        #     "foo ```code2``` ```code3``` jj ```code4```",
        #     "foo <pre>code2</pre> <pre>code3</pre> jj <pre>code4</pre>",
        # ),
        # (
        #     "```code11\ncode12``` foo ```code21\ncode22``` ```code31\ncode32``` jj ```code41\ncode42```",
        #     "<pre>code11<br>code12</pre> foo <pre>code21<br>code22</pre> <pre>code31<br>code32</pre> jj <pre>code41<br>code42</pre>",
        # ),
        (
            'Whether to install NetObserv Flow.\n```\n192.0.2.1:\n  mem: 256\n# global mem limit rate\n"0.0.0.0/32": 64\n```\n',
            'Whether to install NetObserv Flow. <pre><br>192.0.2.1:<br>  mem: 256<br># global mem limit rate<br>"0.0.0.0/32": 64</pre>',
        ),
    ],
)
def test_htmlify_code(text, want):
    a = _htmlify_code(text)
    assert a == want
