# -*- coding: utf-8 -*
# Copyright 2015 Tencent
# Author: Joe Lei <joelei@tencent.com>
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/httplog.log',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'httplog': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOGGING)

__VERSION__ = '1.1'

try:
    from httplog import patcher
    monkey_patch = patcher.monkey_patch
except Exception as error:
    import traceback
    traceback.print_exc()
