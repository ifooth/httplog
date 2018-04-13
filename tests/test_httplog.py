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


def test_urllib2():
    import urllib2
    urllib2.urlopen('https://pypi.doubanio.com/')


def test_httplib2():
    import httplib2
    h = httplib2.Http()
    h.request("https://pypi.doubanio.com/")
