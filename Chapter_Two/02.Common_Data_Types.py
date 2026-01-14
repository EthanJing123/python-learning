# # 常见数据类型 ---> type() 获取指定的字面量或者变量的类型
# print("Hello")
# print(type("Hello"))
#
# print(type(10))#int
# print(type(3.14))#float
# print(type(True))#bool
# print(type(False))#bool
# print(type(None))#NoneType
#
# num = -100
# print(type(num))#int
#
# # 常见数据类型 ---> isinstance(数据, 类型) --> bool值 -->判定数据类型是否是指定的类型, 如果是: True, 否则:False
# print(isinstance(num, int))
# print(isinstance(num, float))
# print(isinstance(num, bool))
#
# #字符串
# #定义字符串的三种方式
# s1 = "Hello"#双引号定义
# s2 = 'Python'#单引号定义
# s3 = """
#     欢迎大家学习Python课程
#     加油!!
#     """#三引号定义(多行字符串)
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# #定义字符串 ---> It's very good
# #转义字符 \' \" \n \t
# msg = 'It\'s vary good'
# print(msg)
#
# msg1 = "It's vary good"
# print(msg1)
#
# msg3 = "Hello的意思就是\"您好\""
# print(msg3)
#
# msg4 = 'Hello的意思就是"您好'
# print(msg4)
#
# print("\t欢迎大家学习Python课程的学习!\n\t加油!")
#
#
#
#
# #字符串拼接
# s1 = "人生苦短" "我用Python" ", OK"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用PYython"
# print("龟叔说:" + msg1 + "," + msg2)
#
#
# #案例
# name = "EthanJing"
# age = 22
# pro = "计算机工学"
# hobby = "Java、Python"
# print("大家好, 我是" + name + ", 今年" + str(age) + "岁, 学习的专业是" + pro + ", 爱好是" + hobby)


#字符串格式化 --> 方式一 :  %s 占位符
# name = "EthanJing"
# age = 22
# pro = "计算机工学"
# hobby = "Java、Python"
# print("大家好, 我是 %s, 今年 %s 岁, 学习的专业是 %s , 爱好是 %s" %(name , age , pro , hobby ))

#字符串格式化 --> 方式二 :  f"..{变量名/表达式}.." --->企业开发推荐方式
name = "EthanJing"
age = 22
pro = "计算机工学"
hobby = "Java、Python"
print(f"大家好, 我是{name}, 今年{age}岁, 学习的专业是{pro}, 爱好是{hobby}" )