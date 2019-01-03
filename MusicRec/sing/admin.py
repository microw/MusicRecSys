# -*- coding: utf-8 -*-
from django.contrib import admin
from sing.models import Sing,SingTag,SingSim

class adminSing(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("sing_id", "sing_name", "sing_music_num", "sing_mv_num",'sing_album_num',"sing_url",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("sing_id", "sing_name", "sing_music_num", "sing_mv_num",'sing_album_num',"sing_url",)
    # 页面右边会出现相应的过滤器选项
    # 排序
    ordering = ("-sing_music_num",)

admin.site.register(Sing, adminSing)

class adminSingTag(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("sing_id", "tag",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("sing_id", "tag",)
    # 页面右边会出现相应的过滤器选项
    list_filter = ("tag",)
    # 排序
    ordering = ("-sing_id",)

admin.site.register(SingTag, adminSingTag)

class adminSingSim(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("sing_id", "sim_sing_id","sim",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("sing_id", "sim_sing_id","sim",)
    # 排序
    ordering = ("-sing_id",)
admin.site.register(SingSim,adminSingSim)