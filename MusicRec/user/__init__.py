# -*-coding: utf-8 -*-
from django.apps import AppConfig

default_app_config = 'user.PrimaryIndexConfig'

class PrimaryIndexConfig(AppConfig):
    name = "user"
    verbose_name = u"用户"