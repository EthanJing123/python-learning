# 字典 -- key不能重复(如果重复, 后面的值, 会覆盖前面的值), key必须得是不可变类型(str, int, float, tuple)
# 定义字典
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
# print(dict1)
# print(type(dict1))
#
# # key必须得是不可变类型(str, int, float, tyuple), 不能是list, set, dict
# dict2 = {0:670, 1.5:600, (1,2):500, ('A', 'B'):688}
# print(dict2)
#
# # 访问
# print(dict1["李慕婉"]) #获取
# dict1["李慕婉"] = 688
# print(dict1)


# ----------------------- 字典 常见操作 ------------------------
# dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# # 查询
# print(dict1["涛哥"]) # 根据key获取value
# print(dict1.get("涛哥")) # 根据key获取value
#
# print(dict1.keys()) # 获取所有的key值
# print(dict1.values()) # 获取所有的value
# print(dict1.items()) # 获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("许立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k} : {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]} : {item[1]}")
#
# for k, v in dict1.items():
#     print(f"{k} : {v}")



"""
    案例:-------------------购物车管理系统----------------
    开发一个购物车管理系统, 实现商品信息的添加, 修改, 删除, 查询和统计功能. 系统使用嵌套字典结构存储商品数据,通过控制台菜单与用户交互.
    具体功能如下:
        1. 添加购物车 : 用户根据提示录入商品名称、以及该商品的价务、数量,保存该商品信息到购物车。
        2. 修改购物车 : 要求用户输入要修改的购物车商品名称,然后再技是示输入该商品的价格、数量,输入完成后修改该商品信息
        3. 删除购物车 : 要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
        4. 直询购物车 : 将购物车中的商品信息展示出来,格式为:I"商品名称:xxx,商品价格:xxxx,商品数量:xxx"。
        5. 退出购物车

    结构:shopping_cart = {"Meta80": {"price": 6999, "num": 2, "鼠标": {...}}

"""

# shopping_cart = {}
# menu = """
# ############### 购物车系统 ################
# #             1. 添加购物车               #
# #             2. 修改购物车               #
# #             3. 删除购物车               #
# #             4. 查询购物车               #
# #             5. 退出购物车               #
# #########################################
#     """
# print("欢迎使用购物车管理系统 ~")
#
# while True:
#     # 1. 制作菜单
#     print(menu)
#
#     # 2. 执行的具体操作
#     choice = input("请选择要执行的操作(1-5):")
#     match choice:
#         case "1": # 添加购物车
#             goods_name = input("请输入商品名称: ")
#             if goods_name in shopping_cart:
#                 print(f"【{goods_name}】已经存在了，如果要调整数量请选择功能2")
#             else:
#                 price = float(input("请输入商品价格: "))
#                 num = int(input("请输入商品数量: "))
#                 # 字典嵌套字典：用商品名做 key
#                 shopping_cart[goods_name] = {"price": price, "num": num}
#                 print("添加成功 ~")
#         case "2": # 修改购物车
#             goods_name = input("请输入要修改的商品名称: ")
#             # 如果商品不存在, 则提示错误信息, 重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在, 请重新选择 ~")
#                 continue
#
#             goods_price = float(input("请输入商品最新的价格: "))
#             goods_num = int(input("请输入商品最新的数量: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕 ~")
#         case "3": # 删除购物车
#             goods_name = input("请输入要删除的商品名称: ")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在, 请重新选择 ~")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕 ~")
#         case "4": # 查询购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称: {goods_name}, 商品价格: {goods_info['price']}, 商品数量: {goods_info['num']}")
#         case "5": # 退出购物车
#             print("bye ~")
#             break
#         case _:
#             print("非法操作,不支持!!!!!!")



"""
    开发一个教务管理系统, 在该系统中可以维护和管理学员的成绩信息, 具体要求如下:
    1. 添加学生信息: 根据提示录入学生姓名, 语文, 数学, 英语成绩, 录入完成保存到系统中.
    2. 修改学生信息: 要求输入要修改的学生姓名, 然后再提示输入语文, 数学, 英语成绩, 输入完成后修改学员信息.
    3. 删除学生信息: 要求输入要删除的学生姓名, 根据姓名删除学生信息.
    4. 查询学生信息: 要求输入要查询的学生姓名, 根据姓名查询学生信息并输出.
    5. 列出所有学生: 遍历所有学生信息并输出.
    6. 统计班级成绩: 统计班级语文, 数学, 英语成绩的最高分, 最低分, 平均分, 以及语文, 数学, 英语最高分和最低分的学生姓名.
    7. 退出系统.
    """
academic_management_system = {}
menu = """
# # # # # # # # # # # # # # # # # # # # # # # #  [菜单] # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1. 添加学生信息  2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用教务管理系统 !")

while True:
    print(menu)
    choice = input("请输入要执行的操作(1-7):").strip()

    match choice:
        case "1":  # 添加
            students_name = input("请输入学生的姓名: ").strip()
            if students_name in academic_management_system:
                print(f"{students_name}学生已存在,如需修改请选2 ~")
            else:
                cn = float(input("请输入语文成绩: "))
                ma = float(input("请输入数学成绩: "))
                en = float(input("请输入英语成绩: "))
                academic_management_system[students_name] = {"chinese": cn, "math": ma, "english": en}
                print("添加成功 ~")

        case "2":  # 修改
            name = input("请输入姓名: ").strip()
            if name not in academic_management_system:
                print("学生不存在。")
            else:
                academic_management_system[name]["chinese"] = float(input("新语文: "))
                academic_management_system[name]["math"] = float(input("新数学: "))
                academic_management_system[name]["english"] = float(input("新英语: "))
                print("修改成功！")

        case "3":  # 删除
            name = input("请输入姓名: ").strip()
            if name in academic_management_system:
                academic_management_system.pop(name)
                print("已删除。")
            else:
                print("学生不存在。")

        case "4":  # 查询
            name = input("请输入姓名: ").strip()
            if name in academic_management_system:
                s = academic_management_system[name]
                print(f"【{name}】 语文:{s['chinese']}, 数学:{s['math']}, 英语:{s['english']}")
            else:
                print("未找到该学生。")

        case "5":  # 列出所有
            if not academic_management_system:
                print("暂无数据。")
            else:
                print("-" * 50)
                for name, info in academic_management_system.items():
                    print(
                        f"姓名: {name:6} | 语文: {info['chinese']:>5} | 数学: {info['math']:>5} | 英语: {info['english']:>5}")
                print("-" * 50)

        case "6":  # 统计成绩
            if not academic_management_system:
                print("没有数据，无法统计 ~")
                continue

            total_cn = total_ma = total_en = 0
            count = 0
            first_time = True

            # --- 循环开始：这里只负责收集数据和比大小 ---
            for name, info in academic_management_system.items():
                cn, ma, en = info["chinese"], info["math"], info["english"]
                total_cn += cn
                total_ma += ma
                total_en += en
                count += 1

                if first_time:
                    max_cn = min_cn = cn
                    max_ma = min_ma = ma
                    max_en = min_en = en
                    max_cn_name = min_cn_name = max_ma_name = min_ma_name = max_en_name = min_en_name = name
                    first_time = False
                else:
                    if cn > max_cn: max_cn, max_cn_name = cn, name
                    if cn < min_cn: min_cn, min_cn_name = cn, name
                    if ma > max_ma: max_ma, max_ma_name = ma, name
                    if ma < min_ma: min_ma, min_ma_name = ma, name
                    if en > max_en: max_en, max_en_name = en, name
                    if en < min_en: min_en, min_en_name = en, name
            # --- 循环结束：缩进回退到和 for 对齐 ---

            # 【重点】打印语句现在在循环外面，所以只会在全部数完后打印一遍
            print("\n" + "=" * 25 + " 班级成绩详细统计表 " + "=" * 25)

            print(f"【语文】 平均分: {total_cn / count:.2f}")
            print(f"       最高分: {max_cn:>6.1f} (学生: {max_cn_name})")
            print(f"       最低分: {min_cn:>6.1f} (学生: {min_cn_name})")
            print("-" * 65)

            print(f"【数学】 平均分: {total_ma / count:.2f}")
            print(f"       最高分: {max_ma:>6.1f} (学生: {max_ma_name})")
            print(f"       最低分: {min_ma:>6.1f} (学生: {min_ma_name})")
            print("-" * 65)

            print(f"【英语】 平均分: {total_en / count:.2f}")
            print(f"       最高分: {max_en:>6.1f} (学生: {max_en_name})")
            print(f"       最低分: {min_en:>6.1f} (学生: {min_en_name})")

            print("=" * 65 + "\n")

        case "7":
            print("退出系统，再见 ~")
            break
        case _:
            print("输入有误，请输入1-7之间的数字 !")









