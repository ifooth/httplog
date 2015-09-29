# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""requests支持
"""
from __future__ import absolute_import
import logging

from requests import sessions, models

LOG_REQ = logging.getLogger('HTTP_REQ')
LOG_RESP = logging.getLogger('HTTP_RESP')


class Session(sessions.Session):
    def request(self, method, url,
                params=None,
                data=None,
                headers=None,
                cookies=None,
                files=None,
                auth=None,
                timeout=None,
                allow_redirects=True,
                proxies=None,
                hooks=None,
                stream=None,
                verify=None,
                cert=None,
                json=None):
        """添加LOG
        """
        req = models.Request(
            method=method.upper(),
            url=url,
            headers=headers,
            files=files,
            data=data or {},
            json=json,
            params=params or {},
            auth=auth,
            cookies=cookies,
            hooks=hooks,
        )
        prep = self.prepare_request(req)

        if prep.method in ['GET']:
            LOG_REQ.info("curl -X %s '%s'" % (prep.method, prep.url))
        else:
            LOG_REQ.info("curl -X %s '%s' -d '%s'" % (
                prep.method, prep.url, prep.body))
        response = super(Session, self).request(
            method, url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookies,
            files=files,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            proxies=proxies,
            hooks=hooks,
            stream=stream,
            verify=verify,
            cert=cert,
            json=json)
        LOG_RESP.info('Resp(%s): %s' % (response.status_code, response.text))
        return response
