# 1.准备商品

shop = [
    ["机械革命",9000],  # shop[ chose][1]
    ["Think pad",4500],
    ["Mac book pro",12000],
    ["洗衣坟",20],
    ["西瓜",2],
    ["老干妈",15],
    ["卫龙辣条",3.5]
]

# 2.准备足够的钱
money = input("请输入初始余额：")
money = int(money) # "5" --> 5



# 3.准备空的购物车
mycart = []



# 4.开始购物：进入商场领取优惠券


while True: # 死循环
    # 展示商品
    for key ,value in enumerate(shop):
        print(key,value)

    # 输入
    import random
    cheap = ["联想电脑5折优惠券", "老干妈6折优惠券","机械革命" ]
    a = random.randint(0, 2)
    b = a  # 优惠券编号
    a = cheap[a]
    print("您已领取：", a)
    print()

    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():# "5" --> 5
        chose = int(chose)
        # 商品是否存在
        if chose  > len(shop): # len()
            print("对不起，您输入商品不存在！别瞎弄！")

        else:
            # 金钱是否足够
            if money < shop[chose][1]:
                print("穷鬼，对不起，钱不够，到其他地方买去！")
                mycart.append(shop[chose])
                money =  money - shop[chose][1]
                print("恭喜，成功添加购物车!,您的余额还剩：￥",money)
                import random


    elif chose == 'q' or chose == 'Q':
       print("欢迎下次光临！拜拜了您嘞！")
    break
else:
     print("对不起，输入非法，请重新输入！别瞎弄！")

# 打印购物小条
print("以下是您的购物小条，请拿好：")
print("--------------Jason 商城------------------")
shop = int(input("商品购买数量"))
for key ,value in enumerate(mycart):
    print(key,value)
print("您的钱包余额还剩：￥",money)
print("-----------------------------------------")



# import pprint
# productList = [('Iphone 8', 10000),
#         ('GTX2080', 8000),
#         ('Z7KP7-GT', 6000),
#         ('Mac pro', 15000),
#         ('Honor 10', 2800),
#         ('Iphone XR', 12000),
#         ('Mi 8', 2999)
#         ]
# shoppingList = []
# print('输入你的工资:')
# salary = input()
# if not salary.isdigit():
#   print('请输入整数')
# else:
#   salary = int(salary)
#
#     for index, item in enumerate(productList):
#       print(index + 1, item)
#     print('输入你要买的商品的序号：')
#     userWant = input()
#     if userWant.isdigit():
#       userWant = int(userWant)
#       if userWant <= len(productList) and userWant > 0:
#         print('你要购买的是：', productList[userWant - 1][0])
#         if salary >= productList[userWant - 1][1]:
#           shoppingList.append(productList[userWant - 1][0])
#           salary -= productList[userWant - 1][1]
#           print('你已经购买了' + productList[userWant - 1][0] + ', 你的余额为 ' + str(salary))
#         else:
#           print('对不起，你的余额不足！请努力工作吧！')
#           print('你当前所购买的商品为：')
#           for brought in shoppingList:
#             pprint.pprint(brought)
#           print('你当前余额为：', salary)
#           exit()
#       else:
#         print('你输入的商品序号有错，请重新输入')
#     elif userWant == 'q':
#       print('-----------Shopping List----------')
#       for brought in shoppingList:
#         pprint.pprint(brought)
#       print('你的余额为 ', salary)
#       exit()
#     else:
#       print('Invalid input！！！')