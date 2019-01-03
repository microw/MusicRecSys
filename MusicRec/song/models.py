# -*-conding: utf-8 -*-
from django.db import models

# 歌曲信息：id,name,专辑id[al]，出版时间[publishTime],歌手信息[ar]，总的评论数，热门评论数，歌曲链接
class Song(models.Model):
    song_id = models.CharField(blank=False, max_length=64, verbose_name="歌曲ID", unique=True)
    song_name = models.CharField(blank=True, max_length=100, verbose_name="歌曲名字")
    song_pl_id = models.CharField(blank=True, max_length=64, verbose_name="专辑ID")
    song_publish_time = models.DateTimeField(blank=True, verbose_name="出版时间")
    song_sing_id = models.CharField(blank=True, max_length=100, verbose_name="歌手ID")
    song_total_comments = models.IntegerField(blank=True,verbose_name="歌曲总的评论数")
    song_hot_comments = models.IntegerField(blank=True,verbose_name="歌曲热门评论数")
    song_url = models.CharField(blank=True, max_length=1000, verbose_name="歌曲链接")
    # song_lysic = models.TextField(blank=True, verbose_name="歌词")

    def __str__(self):
        return self.song_id

    class Meta:
        db_table = 'song'
        verbose_name_plural = "歌曲信息"

class SongLysic(models.Model):
    song_id = models.CharField(blank=False, max_length=64, verbose_name="歌曲ID", unique=True)
    song_lysic = models.TextField(blank=True, verbose_name="歌词")
    def __str__(self):
        return self.song_id
    class Meta:
        db_table = 'songLysic'
        verbose_name_plural = "歌词信息"

class SongTag(models.Model):
    song_id = models.CharField(blank=False, max_length=64, verbose_name="歌曲ID")
    tag = models.CharField(blank=True, max_length=64, verbose_name="歌曲标签")

    def __str__(self):
        return self.song_id

    class Meta:
        db_table = 'SongTag'
        verbose_name_plural = "歌曲标签"

class SongSim(models.Model):
    song_id = models.CharField(blank=True, max_length=64, verbose_name="歌曲ID")
    sim_song_id = models.CharField(blank=True, max_length=64, verbose_name="相似歌曲ID")
    sim = models.FloatField(blank=True, verbose_name="相似度")
    def __str__(self):
        return self.song_id

    class Meta:
        db_table = 'SongSim'
        verbose_name_plural = "歌曲相似"
