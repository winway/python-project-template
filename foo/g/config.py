#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Date : 2018-12-14 15:35:14
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
加载配置文件，维护全局变量
"""

import os
import sys
import yaml

import foo.utils.logger


logger = foo.utils.logger.getLogger()


isLoaded = False

CONFIG = {}


def loadConfig(filename):
    """加载配置文件，更新到全局变量CONFIG"""

    try:
        f = open(filename, mode='r')
        cfg = yaml.load(f)

        global CONFIG
        CONFIG.update(cfg)
        logger.debug('CONFIG: %s' % CONFIG)
    except Exception as e:
        logger.error('loadConfig error: %s' % e)
        sys.exit(1)
    finally:
        f.close()


def getConfig(key):
    """获取配置值"""

    global isLoaded

    if not isLoaded:
        loadConfig(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/conf.yaml')
        isLoaded = True

    value = CONFIG.get(key, None)
    if value is None:
        logger.error('getConfig error: %s' % key)
        sys.exit(1)

    return value
