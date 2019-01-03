# -*- coding: utf-8 -*-

from playlist.models import PlayList
from song.models import Song
from sing.models import Sing

def rankResult():
    result = dict()
    result["code"] = 1
    result["data"] = dict()
    result["data"]["playlist"] = rankPlayLisy()
    result["data"]["song"] = rankSong()
    result["data"]["sing"] = rankSinger()
    return result

# 歌单排行榜
def rankPlayLisy():
    result_pl = list()
    play_lists = PlayList.objects.all()[:25]
    for one in play_lists:
        result_pl.append({
            "pl_id": one.pl_id,
            "pl_creator": one.pl_creator.u_name,
            "pl_name": one.pl_name,
            "pl_img_url": one.pl_img_url
        })
    return result_pl

# 歌曲排行榜
def rankSong():
    result_song = list()
    songs = Song.objects.all()[:25]
    for one in songs:
        result_song.append({
            "song_id": one.song_id,
            "song_name": one.song_name,
            "song_publish_time": one.song_publish_time
        })
    return result_song

# 歌手排行榜
def rankSinger():
    result_sing = list()
    sings = Sing.objects.all()[:25]
    for one in sings:
        result_sing.append({
            "sing_id": one.sing_id,
            "sing_name": one.sing_name,
            "sing_url": one.sing_url
        })
    return result_sing

