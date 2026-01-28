# 注意: 函数定义的时候并不会执行, 只有在调用函数的时候, 函数体的逻辑才会执行; 函数必须先定义. 后调用
# 函数定义
# def out_line():
#     print("---------------------")
#     print("---------------------")
#
# #函数调用
# out_line()


# 函数的参数与返回值
# 函数1: 计算圆的面积 -- 半径
# def circle_area(r):
#     area = 3.14 * r **2
#     return area
# print(circle_area(10))
#
# # 函数2: 计算长方形的面积 -- 长, 宽
# def rectangle_area(l, w):
#     area = l * w
#     return area
# print(rectangle_area(10, 5))

# 函数3: 计算圆的面积和周长 --半径
# def circle_area_len(r):
#     """
#     根据圆的半径, 计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积, 圆的周长
#     """
#     al = round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
#     return al
# al1 = circle_area_len(10)
# print(al1)
#
# area, len = circle_area_len(10) #解包
# print(area)
# print(len)


# 函数的嵌套调用
# def funciton_a():
#     # 调用funciton函数
#     print("a....before")
#     function_b()
#     print("a....after")
# def function_b():
#     print("b....before")
#     function_c()
#     print("b....after")
# def function_c():
#     print("c..")
#
# funciton_a()
#
# print("结束运行~ ")






# 案例1: 定义一个函数: 根据传入进去的底和高计算三角形的面积的函数(三角形的面积 = 底 * 高 / 2).
# def triangle_area(b, h):
#     """
#     根据传入进去的底和高计算三角形的面积
#     :param b: 底
#     :param h: 高
#     :return: 三角形的面积
#     """
#     area = (b * h) / 2
#     return area
#
# b = int(input("请输入三角形的底:"))
# h = int(input("请输入三角形的高"))
# result = triangle_area(b, h)
# print(f"底为{b}, 高为{h}的三角形的面积: {result}")

# 案例2: 定义一个函数: 计算传入的字符中元音字母的个数 (元音字母为: aeiouAEIOU)
# def count_aeiou(s):
#     """
#     计算传入的字符中元音字母的个数
#     :param s: 字符
#     :return: 字符中元音字母的个数
#     """
#     vowels = "aeiouAEIOU"
#     num = 0
#     for w in s:
#         if w in vowels:
#             num += 1
#     return num
# s = input("请输入字符: ")
# result = count_aeiou(s)
# print(f"字符{s}中元音字母个数:{result}")


# 案例3: 定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分, 最低分, 平均分(保留一位小数), 并返回
# def scores_max_min_average(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分, 最低分, 平均分(保留一位小数), 并返回
#     :param score_list: 成绩列表
#     :return: 最高分, 最低分, 平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg_s
# scores = []
# for i in range(5):  # 假设班级5个同学
#     score = float(input(f"请输入第{i+1}个同学成绩: "))
#     scores.append(score)
#
# print(scores_max_min_average(scores))


# 作业1: 定义一个函数, 根据传入的分数, 计算对应的分数等级并返回.
# 分数 >= 90: A, 分数 >= 75: B,分数 >= 60: C, 分数 < 60: D
# def scores_grade(grade_list):
#     """
#     根据传入的分数, 计算对应的分数等级并返回
#     :param grade_list:等级列表
#     :return: 分数等级
#     """
#     grade_leverls = [] #定义一个空的等级列表
#     for scores in grade_list:
#         if scores >= 90:
#             grade_leverls.append('A')
#         elif scores >= 75:
#             grade_leverls.append('B')
#         elif scores >= 60:
#             grade_leverls.append('C')
#         else:
#             grade_leverls.append('D')
#     return grade_leverls
#
# #测试输入
# scores_input = input("请输入成绩, 用空格隔开:")
# scores_list = [float(x) for x in scores_input.split()]
#
# # 调用函数
# print(scores_grade(scores_list))

# 作业2: 定义一个函数, 用于判断一个字符串是否是回文串, 返回bool值
# 定义函数，只负责判断，返回True/False
# def is_palindrome(s):
#     """
#     于判断一个字符串是否是回文串, 返回bool值
#     :param s: bool值
#     :return 返回bool值
#     """"
#     s_clean = s.lower()  # 转小写，不区分大小写
#     return s_clean == s_clean[::-1]  # True 或 False
#
# # 接收用户输入
# user_input = input("请输入字符串: ")
#
# # 调用函数，获取布尔值
# result = is_palindrome(user_input)
#
# # 根据布尔值输出结果
# if result:
#     print(f"{user_input} 是回文")
# else:
#     print(f"{user_input} 不是回文")

# 作业3: 定义一个函数: 完成时间转换功能, 将传入的秒转换为小时, 分钟, 秒.
# def convert_time(total_seconds):
#     hour = total_seconds // 3600
#     minute = total_seconds % 3600 // 60
#     second = total_seconds % 60
#     return f'{hour:02d}:{minute:02d}:{second:02d}'
# total_seconds = int(input('请输入总秒数: '))
# print(convert_time(total_seconds))

# 作业4: 定义一个函数: 根据传入进去的三角形的三个边长, 判定三角形的类型(等边, 等腰, 普通或者不构成三角形)
def triangle_type(a,b,c):
    """
    判断三角形类型
    """
    if a +b < c or b+c < a or c+a < b:
        return "不构成三角形 ~"
    elif a == b == c:
        return "构成等边三角形 ~"
    elif a == b or c == a or b == c:
        return "构成等腰三角形 ~"
    else:
        return  "构成普通三角形 ~"
# triangle_sides1 = float(("请输入三角形的第一个边长: "))
# triangle_sides2 = float(("请输入三角形的第二个边长: "))
# triangle_sides3 = float(("请输入三角形的第三个边长: "))
# a, b, c = triangle_sides1, triangle_sides2, triangle_sides3
a, b, c = map(float, input("请输入三角形的三条边,用空格分开: ").split())
print(triangle_type(a, b, c))
