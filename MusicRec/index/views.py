# -*- coding:utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from index.models import Cate
from user.models import User,UserBrowse
from song.models import Song
from sing.models import Sing
from playlist.models import PlayList

from playlist.views import all as allPlayList
from song.views import all as allSongs
from sing.views import all as allSings
from user.views import all as allUsers,wirteBrowse,getLocalTime
from index.indexTag import GetRecTags
from index.ranking import rankResult
from index import recRight as rec_right

# 用户选择登录
@csrf_exempt
def login(request):
    if request.method == "GET":
        # 返回选择的用户、歌手、歌曲
        users = User.objects.order_by("?").values("u_id","u_name")[:30]
        songs = Song.objects.order_by("?").values("song_id","song_name")[:30]
        sings = Sing.objects.order_by("?").values("sing_id","sing_name")[:20]
        return JsonResponse({
            "code":1,
            "data":{
                "users": { one["u_id"]: one["u_name"] for one in users },
                "songs": { one["song_id"]: one["song_name"] for one in songs },
                "sings": { one["sing_id"]: one["sing_name"] for one in sings }
            }
        })
    else:
        # 将用户信息写入session
        request.session["username"] = request.POST.get("username")
        request.session["sings"] = request.POST.get("sings")
        request.session["songs"] = request.POST.get("songs")
        # 信息进行记录
        wirteBrowse(user_name=request.POST.get("username"),user_click_time=getLocalTime(),desc="登录系统")
        return JsonResponse({
            "code":1,
            "data":{
                "username":request.POST.get("username"),
                "songs": request.POST.get("songs"),
                "sings": request.POST.get("sings")
            }
        })

# 切换用户
def switchuser(request):
    if "username" in request.session.keys():
        uname = request.session["username"]
        # 删除新闻浏览表中的记录
        UserBrowse.objects.filter(user_name=uname).delete()
        print("删除用户: %s 的新闻浏览记录 ..." % uname)
        del request.session["username"]         # 删除session
        del request.session["sings"]         # 删除session
        del request.session["songs"]         # 删除session
        print("用户: %s 执行了切换用户动作，删除其对应的session值 ..." % uname)
    return JsonResponse({"code": 1, "data": {}})

# 获取导航栏
def getCates(request):
    _list = list()
    for cate in Cate.objects.all():
        _list.append({
            "cate_id": cate.cate_id,
            "cate_name": cate.cate_name
        })
    return JsonResponse({
        "code":1,
        "data":_list
    })

# 首页
def home(request):
    _cate = request.GET.get("cateid")
    if "username" not in request.session.keys():  # 如果用户未登陆
        return JsonResponse({"code":0, "data":{}})
    if _cate == "1":    # 为你推荐 返回歌单、歌手、歌曲的tags
        result = GetRecTags(request,request.GET.get("base_click"))
        return JsonResponse(result)
    elif _cate == "6":  # 排行榜
        return JsonResponse( rankResult(request) )
    elif _cate == "7":  # 我的足迹
        return JsonResponse( myBrowse(request) )
    elif _cate == "2":  # 歌单
        return JsonResponse( allPlayList(request) )
    elif _cate == "3":   # 歌曲
        return JsonResponse( allSongs(request) )
    elif _cate == "4":   # 歌手
        return JsonResponse( allSings(request) )
    elif _cate == "5":   # 用户
        return JsonResponse( allUsers(request) )

# 我的足迹
def myBrowse(request):
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    _uname = request.session.get("username")
    result = dict()
    result["code"] = 1
    result["data"] = dict()
    _list = list()
    browses = UserBrowse.objects.filter(user_name=_uname).order_by("user_click_time")
    total = browses.__len__()
    value = ""
    for one in browses[(_page_id -1 ) * 30: _page_id * 30]:
        if one.click_cate == "2":
            value = PlayList.objects.filter(pl_id=one.click_id)[0].pl_name
        elif one.click_cate == "3":
            value = Song.objects.filter(song_id=one.click_id)[0].song_name
        elif one.click_cate == "4":
            if "12797496" in one.click_id:
                value = Sing.objects.filter(sing_id__endswith="12797496")[0].sing_name
            else:
                value = Sing.objects.filter(sing_id=one.click_id)[0].sing_name
        elif one.click_cate == "5":
            value = User.objects.filter(u_id=one.click_id)[0].u_name
        _list.append({
            "username": request.GET.get("username"),
            "time": one.user_click_time,
            "desc": one.desc,
            "name": value
        })
    result["data"]["click"] = _list
    result["data"]["total"] = total
    return result

# 歌单、歌曲、歌手、用户 四个模块的推荐部分
def rec(request):
    _cate = request.GET.get("cateid")
    if "username" not in request.session.keys():
        return JsonResponse({"code": 0, "data": {}})

    if _cate == "2":  # 歌单
        result = rec_right.rec_right_playlist(request)
        return JsonResponse( result )

    elif _cate == "3": # 歌曲
        result = rec_right.rec_right_song(request)
        return JsonResponse( result )

    elif _cate == "4": # 歌手
        result = rec_right.rec_right_sing(request)
        return JsonResponse(result)

    elif _cate == "5": # 用户
        result = rec_right.rec_right_user(request)
        return JsonResponse(result)

    else:  # 其他
        return JsonResponse({"code": 1, "data": {}})