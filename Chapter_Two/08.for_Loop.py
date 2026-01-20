#for循环 : 遍历输入的字符串


# msg = input("请输入需要遍历的字符串:")
#
# for s in msg:
#     print(f"元素:{s}")
# else:
#     print("程序结束!")

#案例1: 计算1-100之间所有奇数的总和
# total = 0 # 记录累加之和

# for i in range(1, 101):
#     if i % 2 == 1:#取模
#         total += i

# for i in range(1, 101, 2):
#     total += i   #简化版本
# print("1-100之间所有奇数的总和:", total)
#
# #案例2: 计算100-500之间所有3的倍数的数字之和
# total = 0 #记录数字之和
# for i in range(100, 501):
#     if i % 3 ==0:
#         total += i
# print("100-500之间所有3的倍数的数字之和:", total)



# 嵌套循环: 根据输入的长方形的长度m, 宽度n, 打印一个长方形
#     如下: 是一个长度为10, 宽度为5 的长方形
#         * * * * * * * * * *
#         * * * * * * * * * *
#         * * * * * * * * * *
#         * * * * * * * * * *
#         * * * * * * * * * *


#1. 接收长方形的长度和宽度
# m = int(input("请输入长方形的长度:"))
# n = int(input("请输入长方形的宽度:"))
#
# for j in range(n):
#     for i in range(m):
#         print("*", end="  ")
#     print()


#嵌套循环案例: 打印99乘法表
for i in range(1, 10): #外层循环 -- 控制行
    for j in range(1, i+1): #内层循环 -- 控制列
        print(f"{j} x {i} = { j * i}", end="    ")
    print()






