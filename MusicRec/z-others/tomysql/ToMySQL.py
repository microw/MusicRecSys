# -*- coding: utf-8 -*-
"""
    Author: Thinkgamer
    Desc:
        代码12-3  把数据写入数据库
"""
import os,django
os.environ["DJANGO_SETTINGS_MODULE"]="MusicRec.settings"
django.setup()
"""
 上边import 解决错误：
 django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not 
 django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
"""

import pymysql
import time
import json
from MusicRec.settings import DB_HOST,DB_PORT,DB_USER,DB_PASSWD,DB_NAME
from playlist.models import PlayListToSongs,PlayListToTag,PlayList
from song.models import SongLysic,Song,SongTag
from user.models import User,UserTag
from sing.models import Sing,SingTag


class ToMySQL:
    def __init__(self):
        self.db = self.__connect()
        self.cursor = self.db.cursor()

    # 连接mysql数据库
    def __connect(self):
        db = pymysql.Connect(DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DB_PORT, charset='utf8')
        return db

    # 将歌曲信息写入数据库 OK
    """
        song_id = models.CharField(blank=False, max_length=64, verbose_name="歌曲ID", unique=True)
        song_name = models.CharField(blank=False, max_length=100, verbose_name="歌曲名字")
        song_pl_id = models.CharField(blank=False, max_length=64, verbose_name="专辑ID")
        song_publish_time = models.DateTimeField(blank=True, verbose_name="出版时间")
        song_sing_id = models.CharField(blank=False, max_length=100, verbose_name="歌手ID")
        song_total_comments = models.IntegerField(blank=True,verbose_name="歌曲总的评论数")
        song_hot_comments = models.IntegerField(blank=True,verbose_name="歌曲热门评论数")
        song_url = models.CharField(blank=True, max_length=1000, verbose_name="歌曲链接")
    """
    def SongMessToMySQL(self):
        for line in open("./data/song_mess_all.txt","r",encoding="utf-8"):
            _list = line.split(" |+| ")
            if _list.__len__() == 9:
                song_id,song_name,song_pl_id,song_publish_time,song_sing_id,song_total_comments,\
                song_hot_comments,size,song_url = line.split(" |+| ")
                s = Song(
                    song_id = song_id,
                    song_name = song_name,
                    song_pl_id = song_pl_id,
                    song_publish_time =self.TransFormTime(int(song_publish_time)/1000),
                    song_sing_id = song_sing_id,
                    song_total_comments = song_total_comments,
                    song_hot_comments = song_hot_comments,
                    song_url = song_url
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(song_id)
                    pass
            else:
                print(line)
        print("Over!")

    # 歌词信息写入数据库 ok
    """
        song_id = models.CharField(blank=False, max_length=64, verbose_name="歌曲ID", unique=True)
        song_lysic = models.TextField(blank=True, verbose_name="歌词")
    """
    def SongLysicToMySQL(self):
        i = 0
        for line in open("./data/song_lysic_mess_all.txt", "r", encoding="utf-8"):
            _list = line.strip().split("\t")
            if _list.__len__() >1:
                songid = _list[0]
                lysic = _list[1]
                if lysic == "null":
                    lysic = "暂无歌词提供！"
                SongLysic(song_id=songid, song_lysic=lysic).save()
            else:
                songid=_list[0]
                lysic = "暂无歌词提供！"
                SongLysic(song_id=songid, song_lysic=lysic).save()
            i += 1
            print(i)
        print("歌词信息写入数据库完成！")

    # 歌手信息写入数据库 ok
    """
        sing_id = models.CharField(blank=False, max_length=64, verbose_name="歌手ID", unique=True)
        sing_name = models.CharField(blank=False, max_length=100, verbose_name="歌手名字")
        sing_music_num = models.IntegerField(blank=False, verbose_name="音乐数目")
        sing_mv_num = models.IntegerField(blank=False, verbose_name="MV数目")
        sing_album_num = models.IntegerField(blank=False, verbose_name="专辑数目")
        sing_url = models.CharField(blank=True, max_length=1000, verbose_name="歌手图片")
    """
    def SingMessToMySQL(self):
        have_write_sing = list()
        for line in open("./data/sing_mess_all.txt","r",encoding="utf-8"):
            _list = line.strip().split(",")
            if _list[0] in have_write_sing:
                continue
            if _list.__len__() == 6:
                sing_id,sing_name,sing_music_num,sing_mv_num,sing_album_num,sing_url = line.strip().split(",")
                s = Sing(
                    sing_id = sing_id,
                    sing_name = sing_name,
                    sing_music_num = sing_music_num,
                    sing_mv_num = sing_mv_num,
                    sing_album_num =sing_album_num,
                    sing_url= sing_url
                )
                try:
                   s.save()
                except Exception as e:
                    print(e)
                    print(sing_id)
                    pass
                have_write_sing.append(sing_id)
            else:
                print(_list)
        print("Over!")

    # 用户信息写入数据库 ok
    """
        u_id = models.CharField(blank=False, max_length=64, verbose_name="用户ID", unique=True)
        u_name = models.CharField(blank=False, max_length=150, verbose_name="用户昵称")
        u_birthday = models.DateField(blank=True, verbose_name="生日")
        u_gender = models.IntegerField(blank=True,verbose_name="用户性别")
        u_province = models.CharField(blank=True, max_length=20, verbose_name="用户省份")
        u_city = models.CharField(blank=True, max_length=20, verbose_name="用户城市")
        u_type = models.CharField(blank=True, max_length=10, verbose_name="用户类型")
        u_tags = models.CharField(blank=True, max_length=1000, verbose_name="用户标签")
        u_img_url = models.CharField(blank=True, max_length=1000, verbose_name="头像链接")
        u_auth_status = models.CharField(blank=True, max_length=10, verbose_name="用户状态")
        u_account_status = models.CharField(blank=True, max_length=10, verbose_name="账号状态")
        u_dj_status = models.CharField(blank=True, max_length=10, verbose_name="DJ状态")
        u_vip_type = models.CharField(blank=True, max_length=10, verbose_name="VIP状态")
        u_sign = models.TextField(blank=True, verbose_name="用户签名")
    """
    def userMessToMySQL(self):
        i =0
        uid_list = list()
        for line in open("./data/user_mess_all.txt","r",encoding="utf-8").readlines():
            if line.split(" |=| ").__len__() < 14:
                continue
            u_id,u_name,u_birthday,u_gender,u_province,u_city,u_type,u_tags,u_img_url,u_auth_status,\
            u_account_status,u_dj_status,u_vip_type,u_sign = line.split(" |=| ")
            if u_id in uid_list:
                continue
            else:
                uid_list.append(u_id)
            try:
                user = User(
                    u_id= u_id,
                    u_name = u_name ,
                    u_birthday = self.TransFormTime(float(int(u_birthday)/1000)) ,
                    u_gender = int(u_gender),
                    u_province = u_province,
                    u_city = u_city,
                    u_type = u_type,
                    u_tags = u_tags.replace("[","").replace("]",""),
                    u_img_url = u_img_url,
                    u_auth_status = u_auth_status,
                    u_account_status = u_account_status,
                    u_dj_status =u_dj_status,
                    u_vip_type =u_vip_type,
                    u_sign = '我就是我是颜色不一样的花火！' if u_sign=="\n" else u_sign
                )
                user.save()
                i+=1
                print(i)
            except Exception as e:
                user = User(
                    u_id=u_id,
                    u_name=u_name,
                    u_birthday=self.TransFormTime(float(int(u_birthday) / 1000)),
                    u_gender=int(u_gender),
                    u_province=u_province,
                    u_city = u_city,
                    u_type=u_type,
                    u_tags=u_tags.replace("[", "").replace("]", ""),
                    u_img_url=u_img_url,
                    u_auth_status=u_auth_status,
                    u_account_status=u_account_status,
                    u_dj_status=u_dj_status,
                    u_vip_type=u_vip_type,
                    u_sign='纵有诗论满腹，却道不尽这魏巍河山！'
                )
                user.save()
                i += 1
                print(i)
                print("Error: {} ,{}".format(u_id,e))

    # 歌单信息写入数据库  ok
    """
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
    """
    def playListMessToMysql(self):
        i=0
        for line in open("./data/pl_mess_all.txt", "r", encoding="utf-8"):
            pl_id, pl_creator, pl_name, pl_create_time, pl_update_time, pl_songs_num, pl_listen_num, \
            pl_share_num, pl_comment_num, pl_follow_num, pl_tags, pl_img_url, pl_desc = line.split(" |=| ")
            try:
                user = User.objects.filter(u_id=pl_creator)[0]
            except:
                user = User.objects.filter(u_id=pl_creator)[0]
            pl = PlayList(
                pl_id = pl_id,
                pl_creator = user,
                pl_name = pl_name,
                pl_create_time = self.TransFormTime(int(pl_create_time)/1000),
                pl_update_time = self.TransFormTime(int(pl_update_time)/1000),
                pl_songs_num = int (pl_songs_num),
                pl_listen_num = int( pl_listen_num ),
                pl_share_num = int( pl_share_num) ,
                pl_comment_num = int (pl_comment_num),
                pl_follow_num = int(pl_follow_num),
                pl_tags = str(pl_tags).replace("[","").replace("]","").replace("\'",""),
                pl_img_url = pl_img_url,
                pl_desc = pl_desc
            )
            pl.save()
            i+=1
            print(i)

    # 歌单和歌曲的di对应信息写入数据库 ok
    """
        pl_id = models.ForeignKey(PlayList, related_name="歌单ID", on_delete=False)
        song_id = models.ForeignKey(Song, related_name="歌曲ID", on_delete=False)
    """
    def playListSingMessToMySQL(self):
        i=0
        for line in open("./data/pl_sing_id.txt","r",encoding="utf-8"):
            pid, sids = line.strip().split("\t")
            for sid in str(sids).split(","):
                try:
                    pls = PlayListToSongs(pl_id=pid, song_id=sid)
                    pls.save()
                    i+=1
                    print(i)
                except Exception as e:
                    print(e,pid,sid)
        print("歌单和歌曲ID对应信息写完毕！")

    # 歌单和歌单tag写入数据库  ok
    def playListTagMessToMySQL(self):
        i = 0
        for line in open("./data/pl_mess_all.txt", "r", encoding="utf-8"):
            _list = line.split(" |=| ")
            pl_id = _list[0]
            tags = _list[10].replace("[","").replace("]","")
            if tags.split(",").__len__() > 1:
                for tag in tags.split(","):
                    PlayListToTag(pl_id=pl_id, tag=tag.replace("\'","").replace(" ","")).save()
                    i += 1
                    print(i)
            else:
                PlayListToTag(pl_id=pl_id,tag=tags.replace("\'","").replace(" ","")).save()
                i += 1
                print(i)
        print("Over !")

    # 歌手和歌手标签、歌曲和歌曲标签 写入数据库
    def SingAndTagMessToMySQL(self):
        # 1、歌手 -> 歌曲
        sing_song_dict = dict()
        if os.path.exists("./data/sing_song.json"):
            sing_song_dict = json.load(open("./data/sing_song.json","r",encoding="utf-8"))
        else:
            for one in Song.objects.all().values("song_id","song_sing_id"):
                if "#" in one["song_sing_id"]:
                    for sing in one["song_sing_id"].split("#"):
                        sing_song_dict[sing] = one["song_id"]
                else:
                    sing_song_dict[one["song_sing_id"]] = one["song_id"]
            json.dump(sing_song_dict,open("./data/sing_song.json","w",encoding="utf-8"))
        print(sing_song_dict)

        # 2、歌曲 -> 歌单 -> 标签
        song_playlist_tag_dict = dict()
        if os.path.exists("./data/song_tag.json"):
            song_playlist_tag_dict = json.load(open("./data/song_tag.json","r",encoding="utf-8"))
        else:
            for one in PlayListToSongs.objects.all():
                pl_tags = PlayList.objects.filter(pl_id=one.pl_id).values("pl_tags")
                if one.song_id in song_playlist_tag_dict.keys():
                    song_playlist_tag_dict[one.song_id] += ", " + pl_tags[0]["pl_tags"]
                else:
                    song_playlist_tag_dict[one.song_id] = pl_tags[0]["pl_tags"]
            json.dump(song_playlist_tag_dict,open("./data/song_tag.json","w",encoding="utf-8"))
        print(song_playlist_tag_dict)

        # 将歌曲 -> 标签信息写入数据库,直接写入数据库数据太多，写入文件，利用工具导入
        # for song in song_playlist_tag_dict.keys():
        #     print(song)
        #     for tag in song_playlist_tag_dict[song].split(","):
        #         SongTag(song_id= song,tag= tag.replace(" ","")).save()
        # fw = open("./data/song_tag.txt","a",encoding="utf-8")
        # for song in song_playlist_tag_dict.keys():
        #     print(song)
        #     song_have_write = list()
        #     for tag in song_playlist_tag_dict[song].split(","):
        #         tag = tag.replace(" ","")
        #         if tag not in song_have_write:
        #             fw.write(song + "," + tag +"\n")
        #             song_have_write.append(tag)
        # fw.close()
        # print("Over !")

        # 将歌手 -> 标签信息写入数据库
        # for sing in sing_song_dict.keys():
        #     print(sing)
        #     songId = sing_song_dict[sing]
        #     for tag in song_playlist_tag_dict[songId].split(","):
        #         SingTag(sing_id=sing, tag= tag).save()
        # print("Over !")
        fw1 = open("./data/sing_tag.txt","a",encoding="utf-8")
        for sing in sing_song_dict.keys():
            print(sing)
            songId = sing_song_dict[sing]
            sing_have_write = list()
            for tag in song_playlist_tag_dict[songId].split(","):
                tag = tag.replace(" ", "")
                if tag not in sing_have_write:
                    fw1.write(sing + "," + tag + "\n")
                    sing_have_write.append(tag)
        fw1.close()
        print("Over !")

    # 将用户 -> 标签写入数据库
    def UserTagMessToMySQL(self):
        for one in PlayList.objects.all():
            print(one)
            for tag in one.pl_tags.split(","):
                UserTag(user_id=one.pl_creator.u_id,tag= tag.replace(" ","")).save()
        print("Over !")


    # 13位时间戳转换为时间
    def TransFormTime(self,t1):
        try:
            dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1))
        except Exception as e:
            print(t1)
            print("%s, %s " %(t1,e))
            dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(0))
        return dt

if __name__ == "__main__":
    tomysql = ToMySQL()
    # tomysql.playListSingMessToMySQL()
    # tomysql.playListMessToMysql() # ok
    # tomysql.userMessToMySQL()   ok
    # tomysql.SongLysicToMySQL()  ok
    # tomysql.SingMessToMySQL() #ok
    # tomysql.SongMessToMySQL() #ok
    # tomysql.playListTagMessToMySQL() #ok
    # tomysql.SingAndTagMessToMySQL()
    # tomysql.UserTagMessToMySQL()