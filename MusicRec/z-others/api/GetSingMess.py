# -*- coding: utf-8 -*-
"""
    Author: Thinkgamer
    Desc: 获取歌手信息
    songs: https://api.imjad.cn/cloudmusic/?type=artist&id=12519065
            歌手id，name，音乐作品数[musicSize]，mv作品数[mvSize]，专辑数[albumSize]，头像链接[picUrl]，热门歌曲信息
"""
import requests
import urllib
class GetSingMess:
    def __init__(self):
        self.artist_url = "https://api.imjad.cn/cloudmusic/?type=artist&id="
        self.song_id_file = "./data/song_mess/songs_mess_all.txt"
        self.sings_mess_file = "./data/sing_mess/sings_mess_all.txt"
        self.error_sing_list = list()
        self.error_sing_file = "./data/sing_mess/sings_mess_error_1.txt"
        self.sing_ids =  self.getSingsIDs()

    # 数据样例：46198  /  211123#813244
    def getSingsIDs(self):
        print("开始加载所有歌手的ID信息 ...")
        sing_ids_list = set()
        for line in open(self.song_id_file,"r",encoding="utf-8").readlines():
            sing_ids = line.strip().split(" |+| ")[4]
            if sing_ids.__contains__("#"):
                for id in sing_ids.split("#"):
                    sing_ids_list.add(id)
            else:
                sing_ids_list.add(sing_ids)
        # for line in open(self.error_sing_file,"r",encoding="utf-8"):
        #     sing_ids_list.add(line.strip())
        print("所有歌手ID信息获取完毕,共有 %s 个歌手 ..." % len(sing_ids_list))
        return list(sing_ids_list)

    # 获取每个歌手的信息
    def getSingMess(self):
        print("开始获取每个歌手的信息 ...")
        i = 0
        for id in self.sing_ids:
            try:
                i += 1
                print("%s - 歌手ID: %s" % (i,id))
                res_json = self.getJson(id)
                artist_list = [
                    str(res_json["artist"]["id"]),
                    str(res_json["artist"]["name"]),
                    str(res_json["artist"]["musicSize"]),
                    str(res_json["artist"]["mvSize"]),
                    str(res_json["artist"]["albumSize"]),
                    str(res_json["artist"]["picUrl"])
                ]
                self.writeToFile(self.sings_mess_file,",".join(artist_list))
            except Exception as e:
                print(e)
                print("歌手id为 %s 的信息获取错误，进行记录 ..." % id)
                self.error_sing_list.append(id)

        # 如果有获取错误的歌手将id写入文件
        if self.error_sing_list.__len__() != 0:
            print("将获取歌手信息错误的id写入文件: %s" % self.error_sing_file)
            self.writeToFile(self.error_sing_file, "\n".join(self.error_sing_list))
        print("歌手信息获取完成 ...")

    # 请求接口
    def getJson(self,id):
        # 设置表头
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
            'Referer': 'http://mail.163.com/'
        }

        url = self.artist_url + str(id)
        res_json = requests.get(url, headers=headers).json()
        return res_json

    # 写入文件
    def writeToFile(self, filename, one):
        fw = open(filename, "a", encoding="utf8")
        fw.write(str(one) + "\n")
        fw.close()

if __name__ == "__main__":
    sing = GetSingMess()
    sing.getSingMess()