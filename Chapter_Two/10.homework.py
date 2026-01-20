# 需求1: 将1-1000之间(含1000)所有5的倍数累加起来
# i = 1
# total = 0
# while i <= 1000:
#     if i % 5 == 0:
#         total = i + total
#     i = i + 1
# print("1-1000之间所有五的倍数累加起来为:", total)

# 需求2: 统计字符串"asdkakaskdfjfaskjadfjka" 字符串中有多少个a和k
msg = "asdkakaskdfjfaskjadfjka"

a_count = 0
k_count = 0

for ch in msg:
    if ch == "a":
        a_count += 1
    if ch == "k":
        k_count += 1
print("a的个数:",a_count)
print("k的个数:",k_count)