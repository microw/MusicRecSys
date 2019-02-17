# -*- coding:utf-8 -*-
"""
    Author: Thinkgamer
    Desc:
        计算歌手相似度
"""
import os
import json

class SingSim:
    def __init__(self):
        self.singTags = self.getSingTags()
        print(self.singTags)
        self.sim = self.getSingSim()
        print(self.sim)

    def getSingTags(self):
        singTagsDict = dict()
        for line in open("./data/sing_tag.txt","r",encoding="utf-8"):
            singId, tag = line.strip().split(",")
            singTagsDict.setdefault(singId,set())
            singTagsDict[singId].add(tag)
        return singTagsDict

    def getSingSim(self):
        sim = dict()
        if os.path.exists("./data/sing_sim.json"):
            sim = json.load(open("./data/sing_sim.json","r",encoding="utf-8"))
        else:
            i = 0
            for sing1 in self.singTags.keys():
                sim[sing1] = dict()
                for sing2 in self.singTags.keys():
                    if sing1 != sing2:
                        j_len = len (self.singTags[sing1] & self.singTags[sing2] )
                        if j_len !=0:
                            result = j_len / len(self.singTags[sing1] | self.singTags[sing2])
                            if sim[sing1].__len__() < 20 or result > 0.8:
                                sim[sing1][sing2] = result
                            else:
                                # 找到最小值 并删除
                                minkey = min(sim[sing1], key=sim[sing1].get)
                                del sim[sing1][minkey]
                i += 1
                print(str(i) + "\t" + sing1)
            json.dump(sim, open("./data/sing_sim.json","w",encoding="utf-8"))
        print("歌曲相似度计算完毕！")
        return sim

    def transform(self):
        fw = open("./data/sing_sim.txt", "a", encoding="utf-8")
        for s1 in self.sim.keys():
            for s2 in self.sim[s1].keys():
                fw.write(s1 + "," + s2 + "," + str(self.sim[s1][s2]) + "\n")
        fw.close()
        print("Over!")

if __name__ == "__main__":
    sing = SingSim()
    sing.transform()