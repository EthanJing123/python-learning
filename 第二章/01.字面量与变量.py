# # # #字面量的写法
# # # print("100")#整数int
# # # print("3.14")#小数/浮点数float
# # # print("Ture")#布尔bool
# # # print("False")#布尔bool
# # # print("Hello Python")#字符串str
# # # print("-----------")#字符串str
# # # print("None")#空值NoneType
# # #
# # # print(True + 2)
# # # print(False - 1)
# # #
# # # # 变量 -----> Python是动态类型语言,一个变量是可以储存不同类型的数据的(但是项目开发中,推荐变量只存储一种类型的数据)
# # # num = 1114.1
# # # print(num)
# # #
# # # num = num + 1
# # # print(num)
# # #
# # # num = "ok"
# # # print(num)
# # #
# # # num = True
# # # print(num)
# # #
# # # a = True
# # # print(a)
# #
# # #案例
# # base = 25.1#基础播放量
# # incr = 50#每个月的新增播放量
# # print("未来第一个月的播放量",base + incr)
# # print("未来第二个月的播放量",base + incr + incr)
# #
# # base , incr = 25.1 , 50
# # print("未来第一个月的播放量",base + incr)
# # print("未来第二个月的播放量",base + incr + incr)
#
# #标识符
# true = 1
# print(true)

# 案例1:现有两个变量,分别为:a = 10,b = 20,现需要将两个变量值交换,然后输出到控制台
# a = 10
# b = 20
#
# c = a
# a = b
# b = c
#
# print(a ,b)


a = 100
b = 200
c = 300

temp = a
a = b
b = c
c = temp


print(a ,b , c)