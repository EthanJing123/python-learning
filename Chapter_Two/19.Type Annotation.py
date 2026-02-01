# 变量定义 - 未指定类型注解
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13300998854", "15425815789", "1394568745"}
options = {"count": 2, "total": 10}
goods = ("手机", 6999, 1)

names.append("X")
names.append(100)
names.append(10.1)

print(names)

# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int | float] = ["A", "C", "E"]
phones2: set[str] = {"13300998854", "15425815789", "1394568745"}
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)


names2.append("X")
names2.append(100)
names2.append(10.1)

print(names2)


def calc_order_cost(*args:tuple[str, float, int], coupon=0, score=0, express=0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额

    :param args: 商品信息（商品名、价格、数量） ---> 如: ("鼠标", 188, 2) ("键盘", 388, 1)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费

    # 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2. 扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3. 扣减积分抵扣
    if total_cost >= 5000:
        # 积分只能整百抵扣，100积分抵1元
        deduct = (score // 100) * 1
        if deduct > total_cost:
            deduct = total_cost
        total_cost -= deduct

    # 4. 添加运费
    total_cost += express

    return total_cost


total = calc_order_cost(("鼠标", 188.8888, 2), ("键盘", 388, 1), ("手机", 6999, 1))
print(total)