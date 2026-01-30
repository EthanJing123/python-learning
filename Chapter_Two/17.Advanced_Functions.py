# -------------------------- 函数 - 变量的作用域 ---------------------------
# 全局变量: 在函数外部或者函数的内部都是可以访问的 ;
# num = 100
#
# # 定义函数
# def circle_area(r):
#     # 布局变量: 只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#
#     global num
#     num = 100000
#     print("num = ", num) # 100000
#
#     return area
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ", num) # 100000



# 调试开关
# debug_mode = False
#
# def enable_debug_mode():
#     global debug_mode
#     debug_mode = True
#     print("调试模式已开启")
#
# def disable_debug_mdoe():
#     global debug_mode
#     debug_mode = False
#     print("调试模式已关闭")


# ------------------- 函数 - 传参方式 -------------------
# 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 传参方式一: 位置参数
# stu = reg_stu("张三", 18, "男", "北京")
# print(stu)
#
# # 传参方式二: 关键字参数
# stu = reg_stu(name="王林", age=28, gender="男", city="北京")
# print(stu)
#
# stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
# print(stu)
#
# # 传参方式三: 位置参数 + 关键字参数
# stu = reg_stu("萧炎", 32, city="南京", gender="男")
# print(stu)


# # -------------------------- 函数 - 默认参数 -----------------------
# # 定义函数
# def reg_stu(name, age, gender="男", city="北京"):
#     print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 调用函数
# stu = reg_stu("王林", 20)
# print(stu)
#
# stu = reg_stu("李慕婉", 18, "女")
# print(stu)
#
# stu = reg_stu("林涛", 35, "男", "南京")
# print(stu)



# --------------------------- 函数 - 不定长关键字参数 -----------------------
def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值: {avg_data}")

    return min_data, max_data,avg_data

# 调用函数
# print(calc_data(2, 7, 9, 10, 45, round=3, print=True ))

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 111, 222, round=4, print=True))










