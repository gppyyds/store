# from threading import  Thread
#
# class PCmanager(Thread):
#
#     def run(self) -> None:
#         for i in range(10000):
#             print("电脑管家正在杀毒，已经杀了",i,"个毒！")
#
#
# class PC360(Thread):
#     def run(self) -> None:
#         for i in range(10000):
#             print("360管家正在杀毒，已经杀了",i,"个毒！")
#
#
# p1 = PCmanager()
# p2 = PC360()
#
#
# p1.run()
# p2.run()
#
#
#
# from threading import Thread
# #  全局车票
# hainan_ticket = 200
#
# import time
# class User(Thread):
#     username = ""
#     count = 0
#
#     def run(self) -> None:
#         #  抢票任务
#         global hainan_ticket  # 使用全局变量
#         while True:
#             if hainan_ticket > 0:
#                 self.count = self.count + 1
#                 hainan_ticket = hainan_ticket - 1
#                 print(self.username,"成功抢了一张票！还剩",hainan_ticket)
#                 time.sleep(0.1)
#             else:
#                 print(self.username,"本次总共抢了",self.count,"张票！")
#                 break
#
# u1 =  User()
# u1.username  = "张三"
#
# u2 =  User()
# u2.username = "旺财"
#
#
# u3 =  User()
# u3.username = "haozong"
#
# u1.start()
# u2.start()
# u3.start()










from threading import Thread
ege = 500
import time
class User1(Thread):

    username = ""
    def run(self) -> None:
        global ege  #使用全局变量
        while True:
            if ege <500:
                ege = ege +1
                print(self.username,"成功制造一个",ege,"蛋挞")
                #time.sleep(0.0001)
                continue
            # else:
            #     print(self.username,"一共制造了",ege,"个蛋挞")




#  全局车票


import time
class User2(Thread):
    username = ""
    money =3000


    def run(self) -> None:
        #  抢票任务
        global ege  # 使用全局变量
        while True:
            if ege > 0:
                self.money = self.money - 20
                ege = ege - 1
                print(self.username,"成功买了一个！还剩",ege)
                #time.sleep(0.01)
                if self.money == 0:

                    print(self.username,"一共花了",3000-self.money,"元！")
                    break
                else:
                    continue


b1 = User1()
b1.username = "郝总"



b =  User2()
b.username  = "井空"

b2 =  User2()
b2.username = "野结衣"

b3 =  User2()
b3.username = "奥特曼"

b4 =  User2()
b4.username = "铠甲勇士"

b5 =  User2()
b5.username = "悟空"

b6 =  User2()
b6.username = "白娘子"

b.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()
b1.start()



