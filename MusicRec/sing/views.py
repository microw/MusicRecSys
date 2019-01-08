# -*- coding:utf-8 -*-
from django.http import JsonResponse
from sing.models import Sing,SingTag,SingSim
from user.views import wirteBrowse,getLocalTime
from song.models import Song
def all(request):
    # 接口传入的tag参数
    tag = request.GET.get("tag")
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    print("Tag : %s, page_id: %s" % (tag,_page_id))
    _list = list()
    # 全部歌手
    if tag == "all":
        sing_tags_list = Sing.objects.all().values("sing_id","sing_name","sing_url").order_by("-sing_id")
        # 拼接歌曲信息
        for one in sing_tags_list[(_page_id - 1) * 30:_page_id * 30]:
            _list.append({
                "sing_id": one["sing_id"],
                "sing_name": one["sing_name"],
                "sing_url": one["sing_url"]
            })
    # 指定标签下的歌手
    else:
        sing_tags_list = SingTag.objects.filter(tag=tag).values("sing_id").order_by("sing_id")
        sing_ids = [ s_one["sing_id"] for s_one in sing_tags_list[(_page_id - 1) * 30:_page_id * 30] ]
        sings_list = Sing.objects.filter(sing_id__in=sing_ids).values("sing_id","sing_name","sing_url")
        for one in sings_list:
            _list.append({
                "sing_id": one["sing_id"],
                "sing_name": one["sing_name"],
                "sing_url": one["sing_url"]
            })
    total = sing_tags_list.__len__()
    return {"code": 1,
            "data": {
                "total": total,
                "sings": _list,
                "tags": getAllSingTags()
            }
        }

# 获取所有歌手标签
def getAllSingTags():
    tags = set()
    for one in SingTag.objects.all().values("tag").distinct().order_by("sing_id"):
        tags.add(one["tag"])
    return list(tags)

def one(request):
    sing_id = request.GET.get("id")
    wirteBrowse(user_name=request.GET.get("username"),click_id=sing_id,click_cate="4", user_click_time=getLocalTime(), desc="查看歌手")
    if "12797496" in sing_id:
        one = Sing.objects.filter(sing_id__endswith="12797496")[0]
    else:
        one = Sing.objects.filter(sing_id=sing_id)[0]
    return JsonResponse({
        "code": 1,
        "data": [
            {
                "sing_id": one.sing_id,
                "sing_name": one.sing_name,
                "sing_music_num": one.sing_music_num,
                "sing_mv_num": one.sing_mv_num,
                "sing_album_num": one.sing_album_num,
                "sing_url": one.sing_url,
                "sing_rec": getRecBasedOne(sing_id),
                "sing_songs":getSingerSong(sing_id)
            }
        ]
    })

# 获取单个歌手的推荐
def getRecBasedOne(sing_id):
    result = list()
    sings = SingSim.objects.filter(sing_id=sing_id).order_by("-sim").values("sim_sing_id")[:10]
    for sing in sings:
        one = Sing.objects.filter(sing_id=sing["sim_sing_id"])[0]
        result.append({
            "id": one.sing_id,
            "name": one.sing_name,
            "img_url": one.sing_url,
            "cate":"4"
        })
    return result

# 获取单个歌手的歌曲
def getSingerSong(sid):
    songs = Song.objects.filter(song_sing_id__icontains=sid)
    result = list()
    for one in songs:
        result.append({
            "song_id": one.song_id,
            "song_name": one.song_name,
            "song_publish_time": one.song_publish_time,
        })
    return result