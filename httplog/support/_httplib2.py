# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""httplib2支持
"""
from __future__ import absolute_import
import logging
import json

import httplib2

LOG_REQ = logging.getLogger('HTTP_REQ')
LOG_RESP = logging.getLogger('HTTP_RESP')


class Http(httplib2.Http):
    def request(self, uri, method="GET", body=None, headers=None,
                redirections=httplib2.DEFAULT_MAX_REDIRECTS,
                connection_type=None, **kwargs):
        """添加LOG
        """
        if body:
            LOG_REQ.info("curl -X %s '%s' -d '%s' " % (method, uri, body))
        else:
            LOG_REQ.info("curl -X %s '%s'" % (method, uri))
        response, content = super(Http, self).request(
            uri, method, body, headers, redirections,
            connection_type, **kwargs)
        #content = json.dumps(json.loads(content), ensure_ascii=False)
        LOG_RESP.info('Resp(%s): %s' % (response.status, content.decode("unicode-escape")))
        return (response, content)
