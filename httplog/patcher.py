# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""monkey patch"""


def monkey_patch():
    try:
        import httplib2
        from httplog.support._httplib2 import Http
        httplib2.Http = Http
        import requests
        from httplog.support._requests import Session
        requests.sessions.Session = Session
    except Exception:
        import traceback
        traceback.print_exc()
