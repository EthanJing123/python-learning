# if条件判断: 如果分数超过680, 我就去清华读书
# score = 700
# if score > 680:
#     print("欢迎你来到清华大学")
#     print("你即将踏入大学生活!!!")
#
# print("----------")

# # if案例: 结合前面学习的输入输出及if条件判断的知识, 完成B站登录功能的实现(正确账号:1888888 , 正确密码:888666)
# # 正确的账号和密码
# ok_account = "1888888"
# ok_password = "888666"
#
# # 1. 接收用户账号和密码
# account = input("请输入您的B站账号: ")
# password = input("请输入您的B站密码: ")
#
# # 2. 判断账号和密码是否全部正确, 如果都正确, 则登陆成功, 进入B站首页
# if account == ok_account and password == ok_password:
#     print("登陆成功!")
#     print("进入B站首页")
#
# # 3. 判断账号和密码是否有错误,如果有任何一个错误,则登录失败,提示错误信息
# if account != ok_account or password != ok_password:
#     print("登录失败!")
#     print("您输入的账号或密码错误!")

# if...else...案例: 结合前面学习的输入输出及if条件判断的知识, 完成B站登录功能的实现(正确账号:1888888 , 正确密码:888666)
# 正确的账号和密码
# ok_account = "1888888"
# ok_password = "888666"
#
# # 1. 接收用户账号和密码
# account = input("请输入您的B站账号: ")
# password = input("请输入您的B站密码: ")
#
# # 2. 判断账号和密码是否全部正确, 如果都正确, 则登陆成功, 进入B站首页
# if account == ok_account and password == ok_password:
#     print("登陆成功!")
#     print("进入B站首页")
#
# else:
#     print("登录失败 !")
#     print("账号或密码错误 !")




#案例1: 根据用户输入的年份, 判断这一年是闰年还是平年(非整百年份, 且能被4整除的年份是闰年; 整百年份(如 1900、 2000) 必须被400整除才是闰年)
# year = int(input("请输入需要判定的年龄:"))
#
# #如果是非整百年份, 且能被4整除 就是闰年, 如果是整百年份, 必须被400整除 也是闰年
# if(year %100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year} 是闰年")
# else:
#     print(f"{year}是平年")



# if..elif..else 案例: 根据用户输入的数字, 判断数字是正数, 还是负数, 还是0
# num = float(input("请输入数字:"))
# if num > 0:
#     print(f"{num}是正数")
# elif num < 0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")

#案例: 根据用户输入的用户名和密码进行登录系统 -->admin/666888  root/547527   zhangsan/123456
# username = input("请输入您的用户名:")
# password = input("请输入您的密码:")
#
# if username  == "admin" and password == "666888":
#     print("登陆成功!")
# elif username == "root" and password == "547527":
#     print("登陆成功!")
# elif username == "zhangsan" and password == "123456":
#     print("登陆成功!")
# else:
#     print("账号或密码错误,请重新输入!")


#案例: 三角形类型判断: 根据输入的三个边的边长(正整数), 判定是等边,等腰,普通三角形,还是不能构成三角形
# 1. 三角形构成条件: 两边之和大于第三条边
# 2. 三角形判定规则:
#       三个边都相等,为等边三角形
#       两个边相等,为等腰三角形
#       三个边都不相等,为普通三角形

#接收三角形的三个边的长度
# a = int(input("请输入三角形的第一个边的长度:"))
# b = int(input("请输入三角形的第二个边的长度:"))
# c = int(input("请输入三角形的第三个边的长度:"))
#
# #判断三角形的类型, pass是一个空语句,   起到语法占位的作用
# if a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("这是一个等边三角形.")
#     elif a == b and b != c:
#         print("这是一个等腰三角形.")
#     else:
#         print("这是一个普通三角形")
# else:
#     print("这三个边不构成三角形!")

#练习 北京居民年度电费费用计算:根据输入的用电度数,计算电费
#  第一档: 2880度以下, 电费单价0.4883元/度
#  第二档: 2880 - 4800度, 电费单价0.5383元/度
#  第三档: 4800度以上, 电费单价0.7883元/度

#接收居民年度用电度数
num = float(input("年度用电总度数:"))

if num < 2880:
    print(f"您的年度电费费用为:{num * 0.4883}")
elif num <= 4800:
    print(f"您的年度电费费用为:{num * 0.5383}")
else:
    print(f"您的年度电费费用为:{num * 0.7883}")