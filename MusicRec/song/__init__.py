# -*-coding: utf-8 -*-
from django.apps import AppConfig

default_app_config = 'song.PrimaryIndexConfig'

class PrimaryIndexConfig(AppConfig):
    name = "song"
    verbose_name = u"歌曲"