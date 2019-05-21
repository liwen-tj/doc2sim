## 余弦距离方法
1. 分词
2. 去除一些停用词（一般是指无实际意义的文字以及标点符号等，比如，“的”， “是”， “也”....）
3. 根据词频构造一个词频向量
4. 计算两个段落的余弦相似度（0~1的数值，越大则越相似）
注：停用词表来源 https://github.com/goto456/stopwords/blob/master/%E4%B8%AD%E6%96%87%E5%81%9C%E7%94%A8%E8%AF%8D%E8%A1%A8.txt

## simHash算法
1. 分词
2. 取出关键字，并计算关键字的权重
3. 对所有的关键字进行普通hash操作，每个关键字对应一个64位
4. 对所有关键字按位加权求和，得到一个汇总向量，正值置1， 负值置0
5. 对两端文本得到的汇总向量计算汉明距离（0~64， 越小则越相似）
这里64位也可以设置成64位
