# # 需求1:将如下多个列表合并为一个列表, 并去重复元素, 排好序(升序)后输出到控制台.
#
# list1 = ["M", "A", "C", "E", "F", "G", "H", "L", "N", "I", "J", "K", "O"]
# list2 = ["X", "Z", "T", "D", "E", "F", "G"]
# list3 = ["W", "A", "S", "D"]
#
# # 1. 合并列表
# num_list = [*list3, *list2, *list1]
# print(num_list)
#
# # 2. 去掉重复元素
# new_list = []
#
# for num in num_list:
#     #判断num_list中是否存在num元素, 如不存在,再添加
#     if num not in new_list:
#         new_list.append(num)
#
# print(new_list)
#
# # 3. 列表元素排序
# new_list.sort()
# print(new_list)



# # 需求2: 将如下列表中能被3 或 5整除的元素提取出来,并获取这些数字对应的平方, 组成一个新的列表.
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# # 1.先将列表中能被3 或 5整除的元素提取出来
# new_list = []
# for num in list1:
#     if num % 3 == 0:
#         new_list.append(num)
#     elif num % 5 == 0:
#         new_list.append(num)
# print(new_list)
#
# # 2.获取对应数字的平方,组成一个新的列表
# num_list = [i**2 for i in new_list]
# print(num_list)

# 需求2简化版本:
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# new_list = [i**2 for i in list1 if (i % 3 == 0) or (i % 5 == 0)]
# print(new_list)






# 需求3: 将如下列表中的正数提取出来,封装一个新的列表.
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

# 提取 list1 中的所有正数，生成新列表
new_list = [i for i in list1 if i > 0]
print(new_list)










