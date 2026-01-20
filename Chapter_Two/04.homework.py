#案例1: 计算输入的三个整数的平均数
# x = int(input("请输入第一个数的值:"))
# y = int(input("请输入第二个数的值:"))
# z = int(input("请输入第三个数的值:"))
#
# average = (x + y + z) / 3
# print("三个整数的平均数为: %.2f " %average)


#案例2:要求输入梯形的上底,下底,高 , 然后计算梯形的面积
# x = float(input("请输入梯形的上底:"))
# y = float(input("请输入梯形的下底:"))
# h = float(input("请输入梯形的高:"))
#
# area = (x + y) * h / 2
# print(f"梯形的面积为:{area:.2f}")


#案例3:要求输入圆的半径,然后计算圆的周长和面积 (周长:2πr , 面积πr**2)
# radius = float(input("请输入圆的半径:"))
# circumference = 2 * math.pi * radius
# area = math.pi * radius * radius
#
# print(f"这个圆的周长为:{circumference:.2f},这个圆的面积为{area:.2f}")

#案例4: 身体质量指数BMI的计算 (BMI = 体重(kg) / 身高 (m)**2)
height = float(input("请输入您的身高 (单位：m):"))
weight = float(input("请输入您的体重 (单位：kg):"))
BMI = weight / (height * height)

print(f"您的BMI值为: {BMI:.2f}")
