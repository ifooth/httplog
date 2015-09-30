# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""monkey patch"""
import traceback


def patch_httplib2():
    try:
        import httplib2
        from httplog.support._httplib2 import Http
        httplib2.Http = Http
    except Exception:
        traceback.print_exc()


def patch_requests():
    try:
        import requests
        from httplog.support._requests import Session
        requests.sessions.Session = Session
    except Exception:
        traceback.print_exc()


def patch_urlopen():
    try:
        import urllib2
        from httplog.support._urllib2 import http_log_wraper
        urllib2.urlopen = http_log_wraper(urllib2.urlopen)
    except Exception:
        traceback.print_exc()


def monkey_patch(httplib2=True, requests=True, urlopen=True):
    if httplib2:
        patch_httplib2()
    if requests:
        patch_requests()
    if urlopen:
        patch_urlopen()
