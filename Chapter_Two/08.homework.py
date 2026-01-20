# 需求1:根据输入的直角边的边长, 打印等腰三角形 (如下为直角边为5的等腰直角三角形)
#     *
#     *   *
#     *   *   *
#     *   *   *   *
#     *   *   *   *   *
# a = int(input("请输入等腰三角形的边长:"))
#
# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         print("*", end="\t")
#     print()


#需求2:根据输入的数字, 打印对应的数字金字塔
# num = int(input("请输入数字:"))
#
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#需求3: 要求打印国际象棋棋盘
 # ■ □ ■ □ ■ □ ■ □
 # □ ■ □ ■ □ ■ □ ■
 # ■ □ ■ □ ■ □ ■ □
 # □ ■ □ ■ □ ■ □ ■
 # ■ □ ■ □ ■ □ ■ □
 # □ ■ □ ■ □ ■ □ ■
 # ■ □ ■ □ ■ □ ■ □
 # □ ■ □ ■ □ ■ □ ■

for i in range(8):
    for j in range(8):
        if (i + j) %2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()





