# pandas是提供高性能应用数据类型和分析工具的第三方库
import pandas as pd
import numpy as np

if __name__ == '__main__':

    # Series类型

    a = pd.Series([1,543,234,53,56])
    # 数据左侧是从0开始的自动索引，最下方输出数据类型dtype:int64 (64位的整数类型)
    print(a)

    # 自定义索引
    b = pd.Series([9,8,7,6],index = ['a','b','c','d'])
    print(b)

    # 标量值创建
    s = pd.Series(25,index = ['a','b','c','d'])
    print(s)

    # 从字典类型创建,d没有，显示NaN
    e = pd.Series({'a':9,'b':8,'c':7},index = ['c','a','b','d'])
    print(e)

    # 从ndarray类型创建
    n = pd.Series(np.arange(5))
    print(n)

    # 获取所有索引
    print(b.index)

    # 获取所有数据
    print(b.values)

    # 判断是否存在
    print(0 in b)

    # 获取
    print(b.get('a'))
    print(b.get('f'))

    # 对齐操作，有相同索引的值相加，不同索引的值不计算，索引并集运算
    A = pd.Series([1,2,3],['c','d','e'])
    B = pd.Series([9,8,7,6],['a','b','c','d'])
    print(A+B)

    # 对象和索引取名
    b.name = '对象'
    b.index.name = '索引列'
    print(b)

    # DataFrame类型

    d = pd.DataFrame(np.arange(10).reshape(2,5))
    print(d)