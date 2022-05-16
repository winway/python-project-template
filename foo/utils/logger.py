#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Date : 2018-12-14 15:38:35
# @Link : https://winway.github.io
# @Version : 0.1
# @Description : 这个家伙很懒，没有留下任何信息
# @History :
# @Other:
#
#      ┏┛ ┻━━━━━┛ ┻┓
#      ┃　　　　　　 ┃
#      ┃　　　━　　　┃
#      ┃　┳┛　  ┗┳　┃
#      ┃　　　　　　 ┃
#      ┃　　　┻　　　┃
#      ┃　　　　　　 ┃
#      ┗━┓　　　┏━━━┛
#        ┃　　　┃   GOD BLESS!
#        ┃　　　┃    NO BUG！
#        ┃　　　┗━━━━━━━━━┓
#        ┃　　　　　　　    ┣┓
#        ┃　　　　         ┏┛
#        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
#          ┃ ┫ ┫   ┃ ┫ ┫
#          ┗━┻━┛   ┗━┻━┛

r"""
日志打印
"""

import os
import logging
from logging.config import fileConfig


logger = None


def getLogger():
    """获取日志logger"""

    global logger
    if not logger:
        fileConfig(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/logging.ini')
        logger = logging.getLogger()

    return logger
