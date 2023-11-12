# 不定长参数2, 转换为字典
# kw可能就是key和value
# **可以类比cpp的二级指针
def unkown_len_func(max, **kwargs):
    print("max_num=",max)
    print(kwargs)
    # kwargs.items()返回一个包含字典所有键值对的迭代器
    # 每个键值对都是一个元组
    for key, value in kwargs.items():
        print("key=",key, " value=", value)
    return 

unkown_len_func(99,求和=3,求最大值=98,长度=3)