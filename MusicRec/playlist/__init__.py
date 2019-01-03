# -*-coding: utf-8 -*-
from django.apps import AppConfig

default_app_config = 'playlist.PrimaryIndexConfig'

class PrimaryIndexConfig(AppConfig):
    name = "playlist"
    verbose_name = u"歌单"