import jieba
import numpy as np

def load_stop_words(filename):
    # 加载停用词表
    with open(filename, encoding='UTF-8') as lines:
        stop_words = [t[:-1] for t in lines]
        return stop_words


def doc_sim(s1, s2, stop_words):
    sc1 = jieba.cut(s1) # 分词
    sc1 = [sc for sc in sc1 if sc not in stop_words] # 去除停用词
    sc2 = jieba.cut(s2) # 分词
    sc2 = [sc for sc in sc2 if sc not in stop_words] # 去除停用词
    
    words = list(set(sc1 + sc2))
    # print(sc1)
    # print(sc2)
    len_words = len(words)
    # v1 v2为词频向量
    v1, v2 = np.zeros(len_words), np.zeros(len_words)
    for sc in sc1:
        v1[words.index(sc)] += 1
    for sc in sc2:
        v2[words.index(sc)] += 1
    print(v1)
    print(v2)
    dis = np.dot(v1, v2) / (np.linalg.norm(v1) * (np.linalg.norm(v2) ))
    return dis


if __name__ == '__main__':
    stop_words = load_stop_words("stopWords")
    dis = doc_sim("传统的Hash算法将内容随机映射为一个签名值。该签名值是完全随机的",
            "SimHash本身属于一种局部敏感哈希算法，它产生的Hash签名在一定程度上可以表征原内容的相似度。",
            stop_words)

    print(dis) # 0.278
    
    dis = doc_sim("SimHash属于局部敏感哈希算法，其Hash签名可以在一定程度上表征原内容的相似度。",
            "SimHash本身属于一种局部敏感哈希算法，它产生的Hash签名在一定程度上可以表征原内容的相似度。",
            stop_words)

    print(dis) # 0.939

    dis = doc_sim("文本相似度计算是自然语言处理中的一项基础性研究,通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究,以便于快速学习和掌握文本相似度计算方法。",
            "相似度计算是自然语言处理工作的基石。随着自然语言处理技术的发展,相似度计算的研究价值和应用价值突显。现有的计算方法因其复杂度和精确度的问题,与现实应用的需求并不匹配。",
            stop_words)

    print(dis) # 0.541

    dis = doc_sim("文本相似度计算是自然语言处理中的一项基础性研究。通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究,以便于快速学习和掌握文本相似度计算方法。",
            "相似度计算是自然语言处理工作的基石。随着自然语言处理技术的发展,相似度计算的研究价值和应用价值突显。通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究。",
            stop_words)

    print(dis) # 0.852

    dis = doc_sim("文本相似度计算是自然语言处理中的一项基础性研究。通过总结和分析文本相似度计算的经典方法和当前最新的研究成果,完善对文本相似度计算方法的系统化研究,以便于快速学习和掌握文本相似度计算方法。",
            "传统的Hash算法将文本内容随机映射为一个签名值。该签名值是完全随机的。",
            stop_words)

    print(dis) # 0.099



