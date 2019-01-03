# -*- coding: utf-8 -*-
from django.http import JsonResponse

from user.models import User,UserBrowse,UserTag,UserSim
import time

def all(request):
    # 接口传入的tag参数
    tag = request.GET.get("tag")
    print("Tag : %s" % tag)
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    print("page_id: %s" % _page_id)
    _list = list()
    # 全部用户
    if tag == "all":
        sLists = User.objects.all().order_by("-u_id")
        # 拼接用户信息
        for one in sLists[(_page_id - 1) * 30:_page_id * 30]:
            _list.append({
                "u_id": one.u_id,
                "u_name": one.u_name,
                "u_img_url": one.u_img_url
            })
    # 指定标签下的用户
    else:
        sLists = UserTag.objects.filter(tag=tag).values("user_id").order_by("user_id")
        sIds = sLists[(_page_id - 1) * 30:_page_id * 30]
        for sid in sIds:
            one = User.objects.filter(u_id=sid["user_id"])
            if one.__len__() == 1:
                one = one[0]
            else:
                continue
            _list.append({
                "u_id": one.u_id,
                "u_name": one.u_name,
                "u_img_url": one.u_img_url
            })
    total = sLists.__len__()
    return {"code": 1,
            "data": {
                "total": total,
                "sings": _list,
                "tags": getAllUserTags()
            }
        }

# 获取所有用户标签
def getAllUserTags():
    tags = set()
    for one in UserTag.objects.all().values("tag").order_by("user_id"):
        tags.add(one["tag"])
    return list(tags)

def one(request):
    u_id = request.GET.get("id")
    one = User.objects.filter(u_id=u_id)[0]
    wirteBrowse(user_name=request.GET.get("username"),click_id=u_id,click_cate="5", user_click_time=getLocalTime(), desc="查看用户")
    return JsonResponse({
        "code": 1,
        "data": [
            {
                "u_id": one.u_id,
                "u_name": one.u_name,
                "u_birthday":one.u_birthday,
                "u_gender":one.u_gender,
                "u_province":one.u_province,
                "u_city":one.u_city,
                "u_tags":one.u_tags,
                "u_img_url": one.u_img_url,
                "u_sign":one.u_sign,
                "u_rec": getRecBasedOne(u_id)
            }
        ]
    })

# 获取单个歌手的推荐
def getRecBasedOne(u_id):
    result = list()
    sim_users = UserSim.objects.filter(user_id=u_id).order_by("-sim").values("sim_user_id")[:10]
    for user in sim_users:
        one = User.objects.filter(u_id= user["sim_user_id"])[0]
        result.append({
            "id": one.u_id,
            "name": one.u_name,
            "img_url": one.u_img_url,
            "cate":"5"
        })
    return result

# 用户浏览信息进行记录
"""
    user_name = models.CharField(blank=False, max_length=64, verbose_name="用户名")
    click_id = models.CharField(blank=False, max_length=64, verbose_name="ID")
    click_cate = models.CharField(blank=False, max_length=64, verbose_name="类别")
    user_click_time = models.DateTimeField(blank=False, verbose_name="浏览时间")
    desc = models.CharField(blank=False, max_length=1000, verbose_name="备注",default="Are you ready!")
"""
def wirteBrowse(user_name="",click_id="",click_cate="",user_click_time="",desc=""):
    if "12797496" in click_id: click_id = "12797496"
    UserBrowse(user_name=user_name,
               click_id=click_id,
               click_cate=click_cate,
               user_click_time = user_click_time,
               desc=desc).save()
    print("用户【 %s 】的行为记录【 %s 】写入数据库" % (user_name, desc))

# 获取当前格式化的系统时间
def getLocalTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())