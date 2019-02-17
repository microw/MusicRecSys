# -*- coding: utf-8 -*-

"""
    Author: Thinkgamer
    Desc:
        基于内容的推荐算法 构建用户的歌单推荐
    Step:
        1、构建用户偏好矩阵（用户->标签的偏好）
        2、构建歌单的特征信息矩阵
"""
import numpy as np
import json
import os

class RecPlayList:
    def __init__(self):
        self.file = "../tomysql/data/pl_mess_all.txt"
        self.tags_list = list()  # 所有标签列表
        self.user_tags_count_dict = dict()  # 用户对标签的次数统计
        self.playlist_tags_dict = dict()  # 歌单和标签对应关系
        self.user_playlist_dict = dict()  # 记录用户有行为的歌单

        self.load_data()

        self.playlist_feature_matrix = self.create_playlist_feature_matrix()
        self.user_feature_prefer_matrix = self.create_user_feature_prefer_matrix()
        self.user_playlist_prefer_dict = self.calculation_user_prefer()


    # 加载数据
    def load_data(self):
        for line in open(self.file, "r", encoding="utf-8"):
            pl_mess_list = line.strip().split(" |=| ")
            playlist_id, user_id, tags = (
                pl_mess_list[0],
                pl_mess_list[1],
                str(pl_mess_list[10]).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            )
            # print(playlist_id, user_id, tags)

            self.user_playlist_dict.setdefault(user_id,list())
            self.user_playlist_dict[user_id].append(playlist_id)

            self.user_tags_count_dict.setdefault(user_id, {})
            self.playlist_tags_dict.setdefault(playlist_id, list())
            for tag in tags.split(","):
                if tag not in self.tags_list:
                    self.tags_list.append(tag)

                self.user_tags_count_dict[user_id].setdefault(tag, 0)
                self.user_tags_count_dict[user_id][tag] += 1

                self.playlist_tags_dict[playlist_id].append(tag)

        print("标签信息 | 用户打标签统计 | 歌单对应标签信息统计 完成 ！")

    # 构建歌单特征信息矩阵
    def create_playlist_feature_matrix(self):
        tags_len = self.tags_list.__len__()
        playlist_feature_matrix = dict()
        for playlist_id in self.playlist_tags_dict.keys():
            f_list = [0] * tags_len
            for tag in self.playlist_tags_dict[playlist_id]:
                index = self.tags_list.index(tag)
                f_list[index] = 1
            playlist_feature_matrix[playlist_id] = f_list
        # print(playlist_feature_matrix)
        print("歌单特征信息矩阵构建完成！")
        return playlist_feature_matrix

    # 构建用户对特征的偏好矩阵
    def create_user_feature_prefer_matrix(self):
        tags_len = self.tags_list.__len__()
        user_feature_prefer_matrix = dict()
        for user_id in self.user_tags_count_dict.keys():
            f_list = [0] * tags_len
            # 计算用户标签的平均分
            u_avg = sum(self.user_tags_count_dict[user_id].values())/self.user_tags_count_dict[user_id].__len__()
            for tag in self.user_tags_count_dict[user_id].keys():
                # 用户对该tag的偏好值
                # 用户给歌单打标签，相当于用户对该标签的评分为1，如果用户多次使用了该标签，评分累加
                # 部分用户对所使用的标签都是 1 次，self.user_tags_count_dict[user_id][tag] - u_avg = 0， +1 避免为0
                prefer = self.user_tags_count_dict[user_id][tag] - u_avg + 1
                index = self.tags_list.index(tag)
                f_list[index] = prefer
            user_feature_prefer_matrix[user_id] = f_list
        # print(user_feature_prefer_matrix)
        print("用户特征标签偏好矩阵构建完成！")
        return user_feature_prefer_matrix

    # 计算用户对歌单的偏好
    def calculation_user_prefer(self):
        user_playlist_prefer_dict = dict()
        if os.path.exists("./data/user_playlist_prefer.json"):
            user_playlist_prefer_dict = json.load(open("./data/user_playlist_prefer.json","r",encoding="utf-8"))
            print("用户对歌单的偏好从文件加载完成")
            return user_playlist_prefer_dict
        for user_id in self.user_feature_prefer_matrix.keys():
            user_playlist_prefer_dict.setdefault(user_id,{})
            for playlist_id in self.playlist_feature_matrix.keys():
                if playlist_id in self.user_playlist_dict[user_id]:
                    continue
                user_matrix = np.array(self.user_feature_prefer_matrix[user_id])
                playlist_matrix = np.array(self.playlist_feature_matrix[playlist_id])

                prefer = np.dot(user_matrix , playlist_matrix)
                if prefer > 0 :
                    user_playlist_prefer_dict[user_id][playlist_id] = prefer
        # print(user_playlist_prefer_dict)
        json.dump(user_playlist_prefer_dict,open("./data/user_playlist_prefer.json","w",encoding="utf-8"))
        print("用户对歌单的偏好计算完成")
        return user_playlist_prefer_dict

    # 将用户对歌单的偏好写入文件，保存每个用户的top 100
    def wrtie_to_file(self):
        fw = open("./data/user_playlist_prefer.txt","a",encoding="utf-8")
        for user_id in self.user_playlist_prefer_dict.keys():
            sorted_user_prefer = sorted(self.user_playlist_prefer_dict[user_id].items(), key = lambda one: one[1], reverse= True)
            for one in sorted_user_prefer[:100]:
                fw.write(user_id+","+one[0]+","+str(one[1])+"\n")
        fw.close()

if __name__ == "__main__":
    rec_pl = RecPlayList()
    rec_pl.wrtie_to_file()