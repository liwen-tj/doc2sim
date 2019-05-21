import math
import jieba
import jieba.analyse
import hashlib
import numpy as np


class SimHash(object):

    def getBinStr(self, source):
        md5 = hashlib.md5(source.encode('utf-8'))
        md516 = md5.hexdigest()[:16]
        hashcode = bin(int(md516, 16))[2:].zfill(64)
        return hashcode
    
    def simHash(self, rawstr):
        seg = jieba.cut(rawstr)
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=100, withWeight=True)
        # print("len(keywords) =", len(keywords), "\n")
        ret = []
        for keyword, weight in keywords:
            binstr = self.getBinStr(keyword)
            keylist = []
            for c in binstr:
                weight = math.ceil(weight)
                if c == "1":
                    keylist.append(int(weight))
                else:
                    keylist.append(-int(weight))
            ret.append(keylist)
            
        res = np.sum(np.array(ret), axis=0) # 转换成np.array，计算速度更快
        result = ""
        for r in res:
            if r > 0: result += "1"
            else: result += "0"
        
        return result

    def getDistince(self, s1, s2):
        hashstr1 = self.simHash(s1)
        hashstr2 = self.simHash(s2)
        length = 0
        for index, char in enumerate(hashstr1):
            if char == hashstr2[index]:
                continue
            else:
                length += 1
        return length


if __name__ == "__main__":
    simhash = SimHash()

    dis = simhash.getDistince("沿着荷塘，是一条曲折的小煤屑路。这是一条幽僻的路；白天也少人走，夜晚更加寂寞。荷塘四面，长着许多树，蓊蓊郁郁的。路的一旁，是些杨柳，和一些不知道名字的树。没有月光的晚上，这路上阴森森的，有些怕人。今晚却很好，虽然月光也还是淡淡的。",
            "沿着一条曲折的小煤屑路。这是一条幽僻的路；荷塘四面，长着许多树，蓊蓊郁郁的。路的一旁，是些杨柳，和一些不知道名字的树。")
    print(dis) # 0.796 16

    dis = simhash.getDistince("传统的Hash算法将内容随机映射为一个签名值。该签名值是完全随机的",
            "SimHash本身属于一种局部敏感哈希算法，它产生的Hash签名在一定程度上可以表征原内容的相似度。")
    print(dis) # 0.278 27

    dis = simhash.getDistince("SimHash属于局部敏感哈希算法，其Hash签名可以在一定程度上表征原内容的相似度。",
            "SimHash本身属于一种局部敏感哈希算法，它产生的Hash签名在一定程度上可以表征原内容的相似度。")
    print(dis) # 0.939 8

    dis = simhash.getDistince("文本相似度计算是自然语言处理中的一项基础性研究,通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究,以便于快速学习和掌握文本相似度计算方法。",
            "相似度计算是自然语言处理工作的基石。随着自然语言处理技术的发展,相似度计算的研究价值和应用价值突显。现有的计算方法因其复杂度和精确度的问题,与现实应用的需求并不匹配。")
    print(dis) # 0.541 30

    dis = simhash.getDistince("文本相似度计算是自然语言处理中的一项基础性研究。通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究,以便于快速学习和掌握文本相似度计算方法。",
            "相似度计算是自然语言处理工作的基石。随着自然语言处理技术的发展,相似度计算的研究价值和应用价值突显。通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究。")
    print(dis) # 0.852 17

    dis = simhash.getDistince("文本相似度计算是自然语言处理中的一项基础性研究。通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究,以便于快速学习和掌握文本相似度计算方法。",
            "传统的Hash算法将文本内容随机映射为一个签名值。该签名值是完全随机的。")
    print(dis) # 0.099 31

    dis = simhash.getDistince("传统的Hash算法将文本内容随机映射为一个签名值。该签名值是完全随机的。",
            "传统的Hash算法将文本内容随机映射为一个签名值。签名值是完全随机。")
    print(dis) # 0.999 0