# -*- coding: utf-8 -*-

from django.db import models
from user.models import User
from song.models import Song

# 歌单信息：歌单ID，创建者ID，名字，创建时间，更新时间，包含音乐数，
#               播放次数，分享次数，评论次数，收藏次数，标签，歌单封面，描述
class PlayList(models.Model):
    pl_id = models.CharField(blank=False, max_length=64, verbose_name="ID", unique=True)
    pl_creator = models.ForeignKey(User, related_name="创建者信息", on_delete=False)
    pl_name = models.CharField(blank=False, max_length=64, verbose_name="歌单名字")
    pl_create_time = models.DateTimeField(blank=True, verbose_name="创建时间")
    pl_update_time = models.DateTimeField(blank=True, verbose_name="更新时间")
    pl_songs_num = models.IntegerField(blank=True,verbose_name="包含音乐数")
    pl_listen_num = models.IntegerField(blank=True,verbose_name="播放次数")
    pl_share_num = models.IntegerField(blank=True,verbose_name="分享次数")
    pl_comment_num = models.IntegerField(blank=True,verbose_name="评论次数")
    pl_follow_num = models.IntegerField(blank=True,verbose_name="收藏次数")
    pl_tags = models.CharField(blank=True, max_length=1000, verbose_name="歌单标签")
    pl_img_url = models.CharField(blank=True, max_length=1000, verbose_name="歌单封面")
    pl_desc = models.TextField(blank=True, verbose_name="歌单描述")

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.pl_id

    class Meta:
        db_table = 'playList'
        verbose_name_plural = "歌单信息"

# 歌单ID 和 歌曲 ID的对应消息
class PlayListToSongs(models.Model):
    pl_id = models.CharField(blank=True, max_length=64, verbose_name="歌单ID")
    # models.ForeignKey(PlayList, related_name="歌单ID", on_delete=False)
    song_id = models.CharField(blank=True, max_length=64, verbose_name="歌曲ID")
    # models.ForeignKey(Song, related_name="歌曲ID", on_delete=False)

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.pl_id

    class Meta:
        db_table = 'playListToSongs'
        verbose_name_plural = "歌曲所属歌单"
# 歌单ID 和 歌曲 ID的对应消息
class PlayListToTag(models.Model):
    pl_id = models.CharField(blank=True, max_length=64, verbose_name="歌单ID")
    tag = models.CharField(blank=True, max_length=64, verbose_name="歌单标签")

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.pl_id

    class Meta:
        db_table = 'playListToTag'
        verbose_name_plural = "歌单标签"
