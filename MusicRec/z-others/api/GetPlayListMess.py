# -*- coding: utf-8 -*-
"""
    Author: Thinkgamer
    Desc:
        获取提供的1066个歌单的信息
"""
import requests
import traceback

# 获取每个歌单的信息类
class PlayList:
    def __init__(self):
        self.playlist_file = "./data/playlist_url/playlist_id_name_all.txt"
        # 获取出错的歌单id保存文件
        self.error_id_file = "./data/error_playlist_ids.txt"
        # 歌单创造者信息
        self.creator_mess = "./data/user_mess/"
        # 每个歌单的json信息
        self.playlist_mess = "./data/playlist_mess/"
        # 歌单包含的歌曲id信息
        self.trackid_mess = "./data/song_mess/"

        self.ids_list = self.getIDs()
        self.url = "https://api.imjad.cn/cloudmusic/?type=playlist&id="
        # 获得的歌单信息出错的歌单id
        self.error_id = list()

    # 由歌单url 获取歌单id
    def getIDs(self):
        print("根据歌单链接获取歌单ID ...")
        ids_list = list()
        for line in open(self.playlist_file,"r",encoding="utf-8").readlines():
            try:
                id = line.strip().split("\t")[0].split("id=")[1]
                ids_list.append(id)
            except Exception as e:
                print(e)
                pass
        print("获取歌单ID完成 ...")
        return ids_list

    # 获取每个歌单的具体信息 url https://api.imjad.cn/cloudmusic/?type=playlist&id=2340739428
    def getEveryPlayListMess(self):
        print("获取每个歌单的具体信息")
        i = 0
        while self.ids_list.__len__() !=0 :
            i += 1
            id = self.ids_list.pop()
            url = self.url + str(id)
            try:
                print("%s - 歌单ID为：%s" % (i,id))
                r = requests.get(url)
                # 解析信息
                self.getFormatPlayListMess(r.json())
            except Exception as e:
                # 获取出错将出错id写入记录一下，然后写入文件，出错时进行跳过
                print(e)
                traceback.print_exc()
                print("歌单ID为：%s 获取出错，进行记录" % id)
                self.error_id.append(id)
                pass
            # break
        self.writeToFile(self.error_id_file,",".join(self.error_id))
        print("歌单信息获取完毕，写入文件: %s" % self.playlist_mess)

    # 每个歌单的内容进行格式化处理 写入文件
    # 需要获取的信息: 歌单信息、创建者信息、歌单音乐信息
    def getFormatPlayListMess(self,json_line):
        # 创建者信息 用户id，昵称，生日，性别，省份，城市，类型，标签，头像链接，用户状态，账号状态，djStatus,vipStatus，签名
        creator = json_line["playlist"]["creator"]
        c_list = (
            str(creator["userId"]),
            str(creator["nickname"]),
            str(creator["birthday"]),
            str(creator["gender"]),
            str(creator["province"]),
            str(creator["city"]),
            str(creator["userType"]),
            str(creator["expertTags"]),
            str(creator["avatarUrl"]),
            str(creator["authStatus"]),
            str(creator["accountStatus"]),
            str(creator["djStatus"]),
            str(creator["vipType"]),
            str(creator["signature"]).replace("\n","")
        )
        self.writeToFile(self.creator_mess + "user_mess_all.txt"," |=| ".join(c_list))

        # 歌单信息
        # 歌单ID，创建者ID，名字，创建时间，更新时间，包含音乐数，播放次数，分享次数，评论次数，收藏次数，标签，歌单封面，描述
        playlist = json_line["playlist"]
        p_list = [
            str(playlist["id"]),
            str(playlist["userId"]),
            str(playlist["name"]).replace("\n",""),
            str(playlist["createTime"]),
            str(playlist["updateTime"]),
            str(playlist["trackCount"]),
            str(playlist["playCount"]),
            str(playlist["shareCount"]),
            str(playlist["commentCount"]),
            str(playlist["subscribedCount"]),
            str(playlist["tags"]),
            str(playlist["coverImgUrl"]),
            str(playlist["description"]).replace("\n","")
        ]
        self.writeToFile(self.playlist_mess + "pl_mess_all.txt"," |=| ".join(p_list))

        # 歌单包含的歌曲信息
        t_list = list()
        trackids = json_line["playlist"]["trackIds"]
        for one in trackids:
            t_list.append(str(one["id"]))
        self.writeToFile(self.trackid_mess + "ids_all1.txt",str(playlist["id"])+"\t"+",".join(t_list))

    # 写入文件
    def writeToFile(self,filename,one):
        fw = open(filename,"a",encoding="utf8")
        fw.write(str(one) + "\n")
        fw.close()

if __name__ == "__main__":
    print("开始获取歌单信息 ..")
    pl = PlayList()
    pl.getEveryPlayListMess()
    print("歌单信息获取完毕 ... Bye !")