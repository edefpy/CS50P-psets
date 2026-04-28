import pytest
from twttr import shorten


def test_lowercase():
    assert shorten("hello, world, today is monday") == "hll, wrld, tdy s mndy"
    assert shorten("just setting up my twitter") == "jst sttng p my twttr"


def test_uppercase():
    assert shorten("HELLO, WORLD, TODAY IS MONDAY") == "HLL, WRLD, TDY S MNDY"
    assert shorten("JUST SETTING UP MY TWITTER") == "JST STTNG P MY TWTTR"


def test_mixed():
    assert shorten("2 HEllo, wORld3, TOday is 1moNDAy") == "2 Hll, wRld3, Tdy s 1mNDy"
    assert shorten("jUSt SETtINg 1up My tWITter 6") == "jSt STtNg 1p My tWTtr 6"
