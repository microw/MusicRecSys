# -*- coding:utf-8 -*-
from django.db import models


# 定义导航栏
class Cate(models.Model):
    cate_id = models.CharField(blank=False, max_length=64, verbose_name='ID', unique=True)
    cate_name = models.CharField(blank=False, max_length=64, verbose_name='名字')

    def __str__(self):
        return self.cate_name

    class Meta:
        db_table = 'cate'
        verbose_name_plural = "导航栏"