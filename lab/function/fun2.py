# 不定长参数1, 转换为元组
def unkown_len_func(max, *args):
    print("max_num=",max)
    print(args)
    print(args[2])
    return 

unkown_len_func(99, 1, 3, 5, 9)