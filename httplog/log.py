# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
"""自定义LOG"""
import logging


class SmartRespHandler(logging.FileHandler):
    def emit(self, record):
        msg = record.getMessage()
        if len(msg) > 1000:
            msg = '%s ... %s' % (msg[:500], msg[-500:])
        record.msg = msg
        super(SmartRespHandler, self).emit(record)
