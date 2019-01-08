# -*- coding:utf-8 -*-
from sing.models import SingTag
from song.models import SongTag
from user.models import UserBrowse
from playlist.models import PlayListToSongs, PlayListToTag

# 首页 推荐标签
"""
    由于标签个数原因，且歌单、歌手、歌曲公用一套标签，所以这里的标签推荐基于
        1、用户进入系统时的选择
        2、用户在站内产生的点击行为
        3、热门标签进行补数
"""

def GetRecTags(request, base_click):
    # 从接口中获取传入的歌手和歌曲id
    sings = request.session["sings"].split(",")
    songs = request.session["songs"].split(",")
    # 歌手标签
    sings_tags = getSingRecTags(sings, base_click)
    # 歌曲标签
    songs_tags,pl_tags = getSongAndPlRecTags(songs, base_click)
    return {
        "code": 1,
        "data": {
            "playlist": {"cateid": 2, "tags": list(pl_tags)},
            "song": {"cateid": 3, "tags": list(songs_tags)},
            "sing": {"cateid": 4, "tags": list(sings_tags)},
        }
    }

# 获得歌手标签推荐
def getSingRecTags(sings, base_click):
    sings_tags = list()
    # base_click =1 表示用户是在站内产生行为后返回为你推荐，此时用户行为对象对应的标签排序在前
    # 否则基于用户选择的标签排序在前
    if base_click == 1:
        click_sings = UserBrowse.objects.filter(click_cate="4").values("click_id")
        if click_sings.__len__() != 0:
            for one in click_sings:
                filter_one = SingTag.objects.filter(sing_id=one["click_id"])
                if filter_one.__len__() != 0 and filter_one[0].tag not in sings_tags:
                    sings_tags.append(filter_one[0].tag)
        if sings.__len__() != 0:  # 表示前端选择了相关歌手
            for sing in sings:
                choose_one = SingTag.objects.filter(sing_id=sing)
                if choose_one.__len__() != 0 and choose_one[0].tag not in sings_tags:
                    sings_tags.append(choose_one[0].tag)
        # print("sings_tags_by_click: %s" % sings_tags_by_click)
    else:
        if sings.__len__() != 0:  # 表示前端选择了相关歌手
            for sing in sings:
                choose_one = SingTag.objects.filter(sing_id=sing)
                if choose_one.__len__() != 0 and choose_one[0].tag not in sings_tags:
                    sings_tags.append(choose_one[0].tag)

        click_sings = UserBrowse.objects.filter(click_cate="4").values("click_id")
        if click_sings.__len__() != 0:
            for one in click_sings:
                filter_one = SingTag.objects.filter(sing_id=one["click_id"])
                if filter_one.__len__() != 0 and filter_one[0].tag not in sings_tags:
                    sings_tags.append(filter_one[0].tag)

    # 如果 click 和 choose的tag不够 以 hot来补充
    if sings_tags.__len__() < 15:
        hot_tag_dict = dict()
        for one in SingTag.objects.all():
            hot_tag_dict.setdefault(one.tag, 0)
            hot_tag_dict[one.tag] += 1
        tag_dict_sing = sorted(hot_tag_dict.items(), key=lambda k: k[1], reverse=True)[:15-sings_tags.__len__()]
        for tag_count in tag_dict_sing:
            if tag_count[0] not in sings_tags:
                sings_tags.append(tag_count[0] )
        # print("sings_tags_by_hot: %s" % sings_tags_by_hot)
    return sings_tags

# 获得歌曲、歌单标签推荐
def getSongAndPlRecTags(songs, base_click):
    song_tags = list()
    pl_tags =  list()
    if base_click == 1: # 表示前端是基于点击行为进入为你推荐模块
        click_songs = UserBrowse.objects.filter(click_cate="3").values("click_id")
        if click_songs.__len__() != 0:
            for one in click_songs:
                filter_one = SongTag.objects.filter(song_id=one["click_id"])
                if filter_one.__len__() != 0 and filter_one[0].tag not in song_tags:
                    song_tags.append(filter_one[0].tag)

                # 歌单tag
                pl_one = PlayListToSongs.objects.filter( song_id=filter_one[0].song_id )
                if pl_one.__len__() !=0:
                    for pl_tag_one in PlayListToTag.objects.filter(pl_id=pl_one[0].song_id):
                        if pl_tag_one.tag not in pl_tags:
                            pl_tags.append(pl_tag_one.tag)

        if songs.__len__() != 0:  # 表示前端选择了相关歌曲
            for sing in songs:
                choose_one = SongTag.objects.filter(song_id=sing)
                if choose_one.__len__() != 0 and choose_one[0].tag not in song_tags:
                    song_tags.append(choose_one[0].tag)

                    # 歌单tag
                    pl_one = PlayListToSongs.objects.filter(song_id=choose_one[0].song_id)
                    if pl_one.__len__() != 0:
                        for pl_tag_one in PlayListToTag.objects.filter(pl_id=pl_one[0].song_id):
                            if pl_tag_one.tag not in pl_tags:
                                pl_tags.append(pl_tag_one.tag)
        # print("songs_tags_by_click %s" % songs_tags_by_click)
        # print("pl_tags_by_click %s" % pl_tags_by_click)
    else:     # 表示用户是首次进入为你推荐模块
        if songs.__len__() != 0:  # 表示前端选择了相关歌曲
            for sing in songs:
                choose_one = SongTag.objects.filter(song_id=sing)
                if choose_one.__len__() != 0 and choose_one[0].tag not in song_tags:
                    song_tags.append(choose_one[0].tag)

                    # 歌单tag
                    pl_one = PlayListToSongs.objects.filter(song_id=choose_one[0].song_id)
                    if pl_one.__len__() != 0:
                        for pl_tag_one in PlayListToTag.objects.filter(pl_id=pl_one[0].song_id):
                            if pl_tag_one.tag not in pl_tags:
                                pl_tags.append(pl_tag_one.tag)
            # print("songs_tags_by_choose: %s" % songs_tags_by_choose)
            # print("pl_tags_by_choose: %s" % pl_tags_by_choose)
    # 如果 click 和 choose的tag不够 以 hot来补充
    if song_tags.__len__() < 15:
        hot_tag_dict = dict()
        for one in SongTag.objects.all():
            hot_tag_dict.setdefault(one.tag, 0)
            hot_tag_dict[one.tag] += 1
        tag_dict_song = sorted(hot_tag_dict.items(), key=lambda k: k[1], reverse=True)[:15-song_tags.__len__()]
        for one in tag_dict_song:
            if one[0] not in song_tags:
                song_tags.append(one[0])
        # print("songs_tags_by_hot: %s" % songs_tags_by_hot)

    # 如果 click 和 choose的tag不够 以 hot来补充
    if pl_tags.__len__() < 15:
        hot_tag_dict = dict()
        for one in PlayListToTag.objects.all():
            hot_tag_dict.setdefault(one.tag, 0)
            hot_tag_dict[one.tag] += 1
        tag_dict_pl = sorted(hot_tag_dict.items(), key=lambda k: k[1], reverse=True)[:15-pl_tags.__len__()]
        for one in tag_dict_pl:
            if one[0] not in pl_tags:
                pl_tags.append(one[0])
        # print("pl_tags_by_hot: %s" % pl_tags_by_hot)

    return song_tags,pl_tags
