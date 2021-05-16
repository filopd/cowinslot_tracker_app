# -*- coding: utf-8 -*-

import pytest
from cowinslot_tracker_app.skeleton import fib

__author__ = "filopd"
__copyright__ = "filopd"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
