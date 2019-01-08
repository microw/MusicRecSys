# -*- coding: utf-8 -*-
from django.contrib import admin
from user.models import User, UserBrowse, UserTag, UserSim, UserUserRec,UserPlayListRec,UserSingRec,UserSongRec


class adminUserMess(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = (
        "u_id",
        "u_name",
        "u_birthday",
        "u_gender",
        "u_province",
        "u_city",
        "u_type",
        "u_auth_status",
        "u_account_status",
        "u_dj_status",
        "u_vip_type",
    )
    # 添加search bar，在指定的字段中searc
    search_fields = (
        "u_id",
        "u_name",
        "u_birthday",
        "u_gender",
        "u_province",
        "u_city",
        "u_type",
        "u_auth_status",
        "u_account_status",
        "u_dj_status",
        "u_vip_type",
    )
    # 页面右边会出现相应的过滤器选项
    list_filter = (
        "u_gender",
        "u_type",
        "u_auth_status",
        "u_account_status",
        "u_dj_status",
        "u_vip_type",
    )
    # 排序
    ordering = ("-u_birthday",)
admin.site.register(User, adminUserMess)


class adminUserBrowse(admin.ModelAdmin):
    list_display = ("user_name", "click_id", "click_cate", "user_click_time", "desc")
    search_fields = ("user_name", "click_id", "click_cate", "user_click_time", "desc")
    list_filter = ("user_name", "click_cate")
    ordering = ("-user_name",)
admin.site.register(UserBrowse, adminUserBrowse)


class adminUserTag(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("user_id", "tag")
    # 添加search bar，在指定的字段中searc
    search_fields = ("user_id", "tag")
    # 页面右边会出现相应的过滤器选项
    list_filter = ("tag",)
    # 排序
    ordering = ("-user_id",)
admin.site.register(UserTag, adminUserTag)


class adminUserSim(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("user_id", "sim_user_id", "sim")
    # 添加search bar，在指定的字段中searc
    search_fields = ("user_id", "sim_user_id", "sim")
    # 排序
    ordering = ("-user_id",)
admin.site.register(UserSim, adminUserSim)


class adminUserUserRec(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("user", "related", "sim",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("user", "related", "sim",)
    # 排序
    ordering = ("-sim",)
admin.site.register(UserUserRec, adminUserUserRec)

class adminUserPlayListRec(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("user", "related", "sim",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("user", "related", "sim",)
    # 排序
    ordering = ("-sim",)
admin.site.register(UserPlayListRec, adminUserPlayListRec)

class adminUserSingRec(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("user", "related", "sim",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("user", "related", "sim",)
    # 排序
    ordering = ("-sim",)
admin.site.register(UserSingRec, adminUserSingRec)

class adminUserSongRec(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("user", "related", "sim",)
    # 添加search bar，在指定的字段中searc
    search_fields = ("user", "related", "sim",)
    # 排序
    ordering = ("-sim",)
admin.site.register(UserSongRec, adminUserSongRec)
