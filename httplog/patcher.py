# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""monkey patch"""
try:
    import httplib2
    from httplog.support.httplib2 import Http
    httplib2.Http = Http
except Exception:
    pass