# -*- coding:utf-8 -*-
from django.http import JsonResponse
from sing.models import Sing,SingTag,SingSim
from user.views import wirteBrowse,getLocalTime
def all(request):
    # 接口传入的tag参数
    tag = request.GET.get("tag")
    print("Tag : %s" % tag)
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    print("page_id: %s" % _page_id)
    _list = list()
    # 全部歌手
    if tag == "all":
        sLists = Sing.objects.all().order_by("-sing_id")
        # 拼接歌曲信息
        for one in sLists[(_page_id - 1) * 30:_page_id * 30]:
            _list.append({
                "sing_id": one.sing_id,
                "sing_name": one.sing_name,
                "sing_url": one.sing_url
            })
    # 指定标签下的歌手
    else:
        sLists = SingTag.objects.filter(tag=tag).values("sing_id").order_by("sing_id")
        sIds = sLists[(_page_id - 1) * 30:_page_id * 30]
        for sid in sIds:
            one = Sing.objects.filter(sing_id=sid["sing_id"])
            if one.__len__() == 1:
                one = one[0]
            else:
                continue
            _list.append({
                "sing_id": one.sing_id,
                "sing_name": one.sing_name,
                "sing_url": one.sing_url
            })
    total = sLists.__len__()
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
    for one in SingTag.objects.all().values("tag").order_by("sing_id"):
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
                "sing_rec": getRecBasedOne(sing_id)
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