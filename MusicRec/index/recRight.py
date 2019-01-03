# -*- coding:utf-8 -*-
from playlist.models import PlayList
from song.models import Song
from sing.models import Sing
from user.models import User

def rec_right_playlist():
    pLists = PlayList.objects.all()
    _list = list()
    for one in pLists:
        _list.append({
            "pl_id": one.pl_id,
            "pl_creator": one.pl_creator.u_name,
            "pl_name": one.pl_name,
            "pl_img_url": one.pl_img_url
        })
    return {"code": 1,
            "data": {
                "recplaylist": _list[:12]
            }
        }


def rec_right_song():
    _list = list()
    for one in Song.objects.all()[:12]:
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

def rec_right_sing():
    _list = list()
    for one in Sing.objects.all()[:12]:
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

def rec_right_user():
    _list = list()
    for one in User.objects.all()[:12]:
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