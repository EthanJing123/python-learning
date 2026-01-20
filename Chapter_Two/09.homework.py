#需求: 根据用户名密码登录, 正确的用户名和密码为admin/666888, zhangsan/123456, taoge/888666,五次登录jihui,输入错误五次,就不允许操作了.
# i = 0
#
# while i < 5:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#
#     if username == "admin" and password == "666888":
#         print("登录成功")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功")
#         break
#     else:
#         print("登录失败,请重新输入")
#         i += 1
#
#     if i == 5:
#         print("您已经输入错误五次,登录失败")


for i in range(5):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    if username == "admin" and password == "666888":
        print("登录成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功")
        break
    else:
        print("登录失败")
        if i == 4:
            print("输入错误五次，不允许再登录")
            break
