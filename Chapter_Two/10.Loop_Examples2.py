"""
    案例2:猜数字游戏
            1. 系统随机生成一个随机数
            2. 用户根据提示猜数字, 并将所猜的数字输入系统
            3. 如果猜错了, 系统给出提示是猜大了, 还是猜小了, 然后继续输入数字
            4. 如果猜对了, 系统自动退出, 游戏结束
"""
import random
random_num = random.randint(1, 100) #生成随机数


while True:
    num = int(input("请输入一个数字: "))

    if num > random_num:
        print("很遗憾,您猜大了!")
    elif num < random_num:
        print("很遗憾,您猜小了")
    else:
        print("恭喜您猜对了!")
        break
print("随机生成的数字为:", random_num)