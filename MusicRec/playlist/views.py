# -*- coding:utf-8 -*-
from django.http import JsonResponse
from playlist.models import PlayList,PlayListToTag,PlayListToSongs
from song.models import Song
from sing.models import Sing
from user.views import wirteBrowse,getLocalTime

from django.db.models import Q


# 获取所有歌单
def all(request):
    # 接口传入的tag参数
    tag = request.GET.get("tag")
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    print("Tag : %s, page_id: %s" % (tag,_page_id))
    if tag == "all":
        pLists = PlayList.objects.all().order_by("-pl_create_time")
    else:
        pLists = PlayList.objects.filter(pl_tags__contains=tag).order_by("-pl_create_time")
    total = pLists.__len__()
    _list = list()
    for one in pLists[(_page_id-1) * 30:_page_id * 30]:
        _list.append({
            "pl_id": one.pl_id,
            "pl_creator": one.pl_creator.u_name,
            "pl_name": one.pl_name,
            "pl_img_url": one.pl_img_url
        })
    return {"code": 1,
            "data": {
                "total": total,
                "playlist": _list,
                "tags": getPlayListTags()
            }
        }

# 获取所有歌单标签
def getPlayListTags():
    tags = set()
    for one in PlayListToTag.objects.all().values("tag").order_by("pl_id"):
        tags.add(one["tag"])
    return list(tags)

# 获取单个歌单信息
def one(request):
    pl_id = request.GET.get("id")
    # 信息进行记录
    wirteBrowse(user_name=request.GET.get("username"),click_id=pl_id,click_cate="2", user_click_time=getLocalTime(), desc="查看歌单")
    one = PlayList.objects.filter(pl_id=pl_id)[0]
    return JsonResponse({
        "code":1,
        "data":[
            {
                "pl_id":one.pl_id,
                "pl_creator": one.pl_creator.u_name,
                "pl_name":one.pl_name,
                "pl_create_time":one.pl_create_time,
                "pl_update_time":one.pl_update_time,
                "pl_songs_num": one.pl_songs_num,
                "pl_listen_num":one.pl_listen_num,
                "pl_share_num":one.pl_share_num,
                "pl_comment_num":one.pl_comment_num,
                "pl_follow_num":one.pl_follow_num,
                "pl_tags": one.pl_tags,
                "pl_img_url":one.pl_img_url,
                "pl_desc":one.pl_desc,
                "pl_rec": getRecBasedOne(pl_id),
                "pl_songs": getIncludeSong(pl_id)
            }
        ]
    })

# 获得单个歌单包含的歌曲
def getIncludeSong(pl_id):
    result = list()
    song_ids = PlayListToSongs.objects.filter(pl_id= pl_id).values("song_id")
    for song in song_ids:
        one = Song.objects.filter(song_id= song["song_id"])[0]
        if "#" in one.song_sing_id:
            sing_name = ""
            for sid in one.song_sing_id.split("#"):
                if sid == "0":
                    sing_name += "," + ""
                else:
                    sing_name += "," + Sing.objects.filter(sing_id=sid)[0].sing_name
        elif one.song_sing_id=="0":
            sing_name=""
        else:
            sing_name = Sing.objects.filter(sing_id= one.song_sing_id)[0].sing_name
        result.append({
            "song_id": one.song_id,
            "song_name": one.song_name,
            "song_sing_name": sing_name,
            "song_url": one.song_url
        })
    return result

# 获取单个歌单的推荐
def getRecBasedOne(pl_id):
    pl_tags = PlayList.objects.filter(pl_id= pl_id).values("pl_tags")[0]["pl_tags"]
    pl_tags_list = pl_tags.replace(" ","").split(",")
    print(pl_tags_list)
    results = list(PlayList.objects.filter(pl_tags=pl_tags).filter(~Q(pl_id=pl_id)))
    if results.__len__() < 10:
        for tag in pl_tags_list:
            for pl in PlayList.objects.filter(pl_tags__contains=tag):
                results.append(pl)
                if results.__len__() >= 10:
                    break
            if results.__len__() >= 10:
                break
    # print(results)
    # 拼接返回结果
    rec_pl_list = list()
    for one in results:
        rec_pl_list.append({
            "id": one.pl_id,
            "name": one.pl_name,
            "creator": one.pl_creator.u_name,
            "img_url": one.pl_img_url,
            "cate": "2"
        })
    return rec_pl_list