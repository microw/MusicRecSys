# -*- coding:utf-8 -*-
from playlist.models import PlayList
from song.models import Song
from sing.models import Sing
from user.models import User,UserSongRec,UserSingRec,UserPlayListRec,UserUserRec

def rec_right_playlist(request):
    user = request.GET.get("username")
    u_id = User.objects.filter(u_name=user)[0].u_id
    rec_all = UserPlayListRec.objects.filter(user=u_id).order_by("-sim")[:12]
    _list = list()
    for rec in rec_all:
        one = PlayList.objects.filter(pl_id=rec.related)[0]
        _list.append({
            "pl_id": one.pl_id,
            "pl_creator": one.pl_creator.u_name,
            "pl_name": one.pl_name,
            "pl_img_url": one.pl_img_url
        })
    return {"code": 1,
            "data": {
                "recplaylist": _list
            }
        }


def rec_right_song(request):
    user = request.GET.get("username")
    u_id = User.objects.filter(u_name=user)[0].u_id
    rec_all = UserSongRec.objects.filter(user=u_id).order_by("-sim")[:12]
    _list = list()
    for rec in rec_all:
        one = Song.objects.filter(song_id=rec.related)[0]
        _list.append({
            "song_id": one.song_id,
            "song_name": one.song_name,
            "song_publish_time": one.song_publish_time,
        })
    return {"code": 1,
            "data": {
                "songs": _list
            }
        }

def rec_right_sing(request):
    user = request.GET.get("username")
    id = User.objects.filter(u_name=user)[0].u_id
    rec_all = UserSingRec.objects.filter(user=id).order_by("-sim")[:12]
    _list = list()
    for rec in rec_all:
        one = Sing.objects.filter(sing_id=rec.related)[0]
        _list.append({
            "sing_id": one.sing_id,
            "sing_name": one.sing_name,
            "sing_url": one.sing_url
        })
    return {"code": 1,
            "data": {
                "sings": _list
            }
        }

def rec_right_user(request):
    user = request.GET.get("username")
    id = User.objects.filter(u_name=user)[0].u_id
    rec_all = UserUserRec.objects.filter(user=id).order_by("-sim")[:12]
    _list = list()
    for rec in rec_all:
        one = User.objects.filter(u_id=rec.related)[0]
        _list.append({
            "u_id": one.u_id,
            "u_name": one.u_name,
            "u_img_url": one.u_img_url
        })
    return {"code": 1,
            "data": {
                "users": _list
            }
        }