# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""httplib2支持
"""
from __future__ import absolute_import
import logging

import httplib2

LOG = logging.getLogger('httplog')


class Http(httplib2.Http):
    def request(self, uri, method="GET", body=None, headers=None,
                redirections=httplib2.DEFAULT_MAX_REDIRECTS,
                connection_type=None, **kwargs):
        """添加LOG
        """
        if body:
            LOG.info("curl -X %s %s -d '%s' " % (method, uri, body))
        else:
            LOG.info("curl -X %s %s" % (method, uri))
        response, content = super(Http, self).request(
            uri, method, body, headers, redirections,
            connection_type, **kwargs)
        LOG.info('Resp: %s' % response)
        return (response, content)
