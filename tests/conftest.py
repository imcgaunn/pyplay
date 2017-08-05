#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for pyplay.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""
from __future__ import print_function, absolute_import, division

import pytest


@pytest.fixture()
def feed_data():
    with open('data/example_feed.rss') as f:
        return f.read()
