# lghDL
~ 项目入口

## 入学任务
### 原始数据分析
```
幸福之路
第一章 　 什么 使人 不幸


动物 只要 不患 疾病 ， 食物 充足 ， 就 会 快乐 满足 。 人 也 应该 如此 ； 然而 现实 并非 这样 ， 至少 在 大多数 情况 下 并非 这样 。 假如 你 是 不幸 的 ， 你 或许 就 会 承认 ， 自己 在 这 一方面 并 不是 个 例外 。 假如 你 是 幸福 的 ， 请 自问 一下 ， 你 的 朋友 中有 几个 是 幸福 的 。 当 你 对 自己 的 朋友 作 了 一番 评论 之后 ， 你 就 应该 学会 察言观色 之术 ， 使 自己 更 善于 感受 日常生活 中 所 遇到 的 人们 的 各种 情绪 。 布莱克 说 ：
```

- 已将 词 用空格隔开
- 排除'幸福之路 第一章'...如果上榜了的话. 

### 引入数据
- 打开方式
    - open('.txt','r').read() 打开后是字符串, 其他的方式如 for line in readlines. 这种不是字符串.

### 清洗
- 去除中文标点

## 统计
### 方法1 python list 及 collection 统计 在命令行实现. 
- 出现频率最高的前 10 个「二元词组」，并输出它们的频率。
    + 二元词组 -> 筛选 列表
        + 「二元词组」即文章中所有接连出现的两个词，如「今天 天气 不错」有「今天 天气」，「天气 不错」两个「二元词组」。
        + 问题: 一个字的算不算是词呢? 应该算吧.
    + 将二元词组列表
    + 频率最高 -> 排序 
    + 频率 -> 统计次数
    + 输出 -> 列表 格式
-> 代码 见 src/listCollection.py

### 方法2 numpy 统计(待尝试)
- 将列表变成数组
- 用 np自带的统计前十来试试. 


## 工具
- python 
- collection



## 关联
- [Zhon — Zhon 1.1.5 documentation](http://zhon.readthedocs.io/en/latest/)
- [https://docs.python.org/3.6/library/collections.html#collections.Counter](https://docs.python.org/3.6/library/collections.html#collections.Counter)
- [5. Data Structures — Python 3.6.3rc1 documentation](https://docs.python.org/3/tutorial/datastructures.html#)
- [4. More Control Flow Tools — Python 3.6.3rc1 documentation](https://docs.python.org/3/tutorial/controlflow.html)
- [5. Built-in Types — Python 2.7.14 documentation](https://docs.python.org/2/library/stdtypes.html)
- [Python Data Science Handbook | Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)
- [numpy.bincount — NumPy v1.13 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.bincount.html)
- [numpy.unique — NumPy v1.10 Manual](https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.unique.html)
- [numpy - How to count the occurrence of certain item in an ndarray in Python? - Stack Overflow](https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray-in-python)
- [python - numpy: most efficient frequency counts for unique values in an array - Stack Overflow](https://stackoverflow.com/questions/10741346/numpy-most-efficient-frequency-counts-for-unique-values-in-an-array)
