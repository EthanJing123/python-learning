# 常见数据类型 ---> type() 获取指定的字面量或者变量的类型
print("Hello")
print(type("Hello"))

print(type(10))#int
print(type(3.14))#float
print(type(True))#bool
print(type(False))#bool
print(type(None))#NoneType

num = -100
print(type(num))#int

# 常见数据类型 ---> isinstance(数据, 类型) --> bool值 -->判定数据类型是否是指定的类型, 如果是: True, 否则:False
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))
