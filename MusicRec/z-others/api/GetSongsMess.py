# -*- coding: utf-8 -*-
"""
    Author: Thinkgamer
    Desc:
        获取每首歌的信息
    songs: https://api.imjad.cn/cloudmusic/?type=detail&id=1330960061
            id,name,歌手信息[ar]，专辑id[al]，出版时间[publishTime]
           https://api.imjad.cn/cloudmusic/?type=comments&id=1330960061
            评论数，热门评论数
           https://api.imjad.cn/cloudmusic/?type=song&id=1330960061
            歌曲链接，大小
           https://api.imjad.cn/cloudmusic/?type=lyric&id=1330960061
            歌词
"""
import requests
class GetSongMess:
    def __init__(self):
        self.detail_url = "https://api.imjad.cn/cloudmusic/?type=detail&id="
        self.song_url = "https://api.imjad.cn/cloudmusic/?type=song&id="
        self.comments_url = "https://api.imjad.cn/cloudmusic/?type=comments&id="
        self.lyric_url = "https://api.imjad.cn/cloudmusic/?type=lyric&id="

        # 保存 获取失败的id
        self.error_ids = list()
        self.error_ids_file = "./data/song_mess/error_ids_1.txt"

        # 记录所有id的文件 合并 获取所有 歌曲id
        self.ids_all_file = "./data/song_mess/"
        self.song_ids = self.getSongIDs()

    # 获取所有的歌曲id信息
    def getSongIDs(self):
        #  获取所有的歌曲id信息
        ids_list = set()
        print(" 获取所有的歌曲id信息 ...")
        for line in open(self.ids_all_file+"ids_all.txt", "r").readlines():
            try:
                for id in line.strip().split(","):
                    ids_list.add(id)
            except Exception as e:
                print(e)
                pass
        print("歌曲ID数为： %s" % ids_list.__len__())
        # for line in open(self.error_ids_file,"r",encoding="utf-8"):
        #     ids_list.add(line.strip())
        # print(list(ids_list).__len__())
        return list(ids_list)

    def getSongMess(self):
        print("开始获取歌曲信息 ...")
        i = 0
        for id in self.song_ids:
            try:
                print("%s - 歌曲id： %s" % (i,id))
                # deatil => id,name,专辑id[al]，出版时间[publishTime],歌手信息[ar]
                url_1 = self.detail_url + str(id)
                res_1_json = requests.get(url_1).json()["songs"][0]
                url_1_list=[
                    str(res_1_json["id"]),
                    str(res_1_json["name"]),
                    str(res_1_json['al']["id"]),
                    str(res_1_json["publishTime"]),
                    "#".join([ str(one["id"]) for one in res_1_json['ar'] ] )
                ]
                # comments => 总的评论数，热门评论数
                url_2 = self.comments_url + str(id)
                res_2_json = requests.get(url_2).json()
                try:
                    url_2_list = [
                        str(res_2_json["total"]),
                        str( len(res_2_json["hotComments"])  )
                    ]
                except:
                    url_2_list = ["0", "0"]
                # lysic => 歌词
                # song => 大小，歌曲链接
                url_3 = self.song_url + str(id)
                res_3_json = requests.get(url_3).json()["data"][0]
                url_3_list = [
                    str(res_3_json["size"]),
                    str(res_3_json["url"])
                ]
                try:
                    url_4 = self.lyric_url + str(id)
                    lysic = requests.get(url_4).json()["lrc"]["lyric"]
                    lysic = lysic.replace("\n","\\n")
                except:
                    lysic = "null"
                self.writeToFile(self.ids_all_file + "songs_mess_all.txt"," |+| ".join(url_1_list + url_2_list + url_3_list ))
                self.writeToFile(self.ids_all_file + "songs_lysics_all.txt", str(res_1_json["id"]) + "\t" + lysic)
                i += 1
            except Exception as e:
                print("error: %s" % e)
                self.error_ids.append(id)
                pass

        # 如果有获取错误的歌曲将id写入文件
        if self.error_ids.__len__() != 0:
            print("将获取歌曲信息错误的id写入文件: %s" % self.error_ids_file)
            self.writeToFile(self.error_ids_file,",".join(self.error_ids))
        print("歌曲信息获取完成 ...")

    # 写入文件
    def writeToFile(self,filename,one):
        fw = open(filename,"a",encoding="utf8")
        fw.write(str(one) + "\n")
        fw.close()


    def filterId(self):
        ids_list_not = list()
        for line in open(self.ids_all_file + "songs_mess.txt","r", encoding="utf-8").readlines():
            id = line.strip().split(" |+| ")[0]
            ids_list_not.append(id)
        i=0
        for one in self.song_ids:
            if one not in ids_list_not:
                print(i)
                i+=1
                self.writeToFile(self.ids_all_file + "not_get_ids_%s.txt" % str(int(i/50000)),one)

if __name__ == "__main__":
    print("开始获取所有歌曲的信息")
    song = GetSongMess()
    song.getSongMess()
