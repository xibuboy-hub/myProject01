# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/7 18:40
*  @Project :   flask_01
*  @FileName:   settings.py
**************************************
程式用途:app配置文件
"""
from datetime import datetime


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = True
    DATABASE_URI = ''


class TestingConfig(Config):
    TESTING = True
