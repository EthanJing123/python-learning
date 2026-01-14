# name = input("请输入你的名字:")
# age = input("请输入你的年龄:")
#
# print(f"您的姓名是:{name} , 您的年龄是:{age}")

#案例
# 总金额
total = 10000

# 1. 输入密码
password = input("请输入密码:")
print(f"密码正确, {password}")

# 2. 输入取款金额
num = input("请输入取款金额:")

# 3.计算余额并输出 --->num 转为 int类型 -->int(num)
print(f"取款后银行卡余额为: {total - int(num)}")