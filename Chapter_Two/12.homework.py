# 需求1: 输入一个字符串,判断该字符串是否是回文(两边对称).
# 1. 接收用户输入的字符串
# str = input("请输入一个字符串")
#
# # 2. 反转字符串
# rev_str = str[::-1]
#
# # 3. 判断是否对称
# if str == reversed_str:
#     print(f"{str}是回文")
# else:
#     print(f"{str}不是回文")


# 需求2: 将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表的内容, 遍历输出出来.
result_list = []

# 接收,反转,大写,存入
for i in range(10):
    s = input("请输入字符串:")

    #反转
    rev_s = s[::-1]

    #大写
    new_s = rev_s.upper()

    #存入列表
    result_list.append(new_s)

for item in result_list:
    print(item)







