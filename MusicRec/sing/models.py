# -*-conding: utf-8 -*-
from django.db import models

# 歌手信息：id,name,musicSize，MVSize,AlbumSize headPic
class Sing(models.Model):
    sing_id = models.CharField(blank=False, max_length=64, verbose_name="歌手ID", unique=True)
    sing_name = models.CharField(blank=True, max_length=100, verbose_name="歌手名字")
    sing_music_num = models.IntegerField(blank=True, verbose_name="音乐数目")
    sing_mv_num = models.IntegerField(blank=True, verbose_name="MV数目")
    sing_album_num = models.IntegerField(blank=True, verbose_name="专辑数目")
    sing_url = models.CharField(blank=True, max_length=1000, verbose_name="歌手图片")

    def __str__(self):
        return self.sing_id
    class Meta:
        db_table = 'sing'
        verbose_name_plural = "歌手信息"

class SingTag(models.Model):
    sing_id = models.CharField(blank=False, max_length=64, verbose_name="歌手ID")
    tag = models.CharField(blank=True, max_length=64, verbose_name="歌手标签")

    def __str__(self):
        return self.sing_id

    class Meta:
        db_table = 'SingTag'
        verbose_name_plural = "歌手标签"

class SingSim(models.Model):
    sing_id = models.CharField(blank=True, max_length=64, verbose_name="歌手ID")
    sim_sing_id = models.CharField(blank=True, max_length=64, verbose_name="相似歌手ID")
    sim = models.FloatField(blank=True,verbose_name="相似度")
    def __str__(self):
        return self.sing_id
    class Meta:
        db_table = "SingSim"
        verbose_name_plural="歌手相似"