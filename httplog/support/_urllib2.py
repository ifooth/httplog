# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""urllib2 urlopen支持"""
from __future__ import absolute_import
import logging
from functools import wraps

LOG_REQ = logging.getLogger('HTTP_REQ')
LOG_RESP = logging.getLogger('HTTP_RESP')


def http_log_wraper(open_func):
    """urlopen装饰器
    """
    @wraps(open_func)
    def _wrapped_view(url, data=None, **kwargs):
        if data:
            LOG_REQ.info("curl -X POST '%s' -d '%s'" % (url, data))
        else:
            LOG_REQ.info("curl -X GET '%s'" % url)
        resp = open_func(url, data, **kwargs)
        content = resp.read()
        LOG_RESP.info('RESP(%s) %s' % (resp.code, content))
        resp.read = lambda: content
        return resp
    return _wrapped_view
