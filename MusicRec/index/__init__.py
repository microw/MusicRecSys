# -*-coding: utf-8 -*-
from django.apps import AppConfig

default_app_config = 'index.PrimaryIndexConfig'

class PrimaryIndexConfig(AppConfig):
    name = "index"
    verbose_name = u"导航栏配置"