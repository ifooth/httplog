# -*- coding: utf-8 -*-
import os.path
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from httplog import patcher
patcher.monkey_patch()


def test_requests():
    import requests
    requests.get('https://pypi.doubanio.com/')
