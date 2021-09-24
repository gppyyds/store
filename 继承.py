import time
class oldphone:
    _username = ""
    number = ""
    bank = ""
    addree =""

    def setusername(self, username):
        self._username = username

    def getusername(self):
        return self._username
    def call(self,number):
        print(self._username,"正在拨号",number)
        for i in range(8):
            print(".",end="")
            time.sleep(1)
        print(self.username,"正在用",self.bank,"手机给",self.addree,"打电话")
        print("品牌为：",self.bank,"很好用")

class newphone(oldphone):
    mucik = ""

    def call(self,number):
        super().call(number)

        self.mucik = True
        print("已拨通，正在响铃", self.mucik)


b = newphone()
b.number = "1232455789"
b.username = "太君"
b.bank = "apple"
b.addree = "北京"
b.mucik = "凤凰传奇"
b.call("15647899")


a = oldphone()
a.number = "1232455789"
a.username = "太君"
a.bank = "apple"
a.addree = "北京"

a.call("15647899")


class cook:
    username = ""
    age = ""

    def setusername(self, username):
        self.username = username

    def getusername(self):
        return self.username

    def setage(self, age):
        if age < 60 and age > 15:
            print("请重新查找")
        else:
            self.age = age

    def zhengcai(self):
        print(self.username, "岁", "蒸菜")

    def chaocai(self):
        print(self.username,  "岁", "炒菜")


class tudi(cook):
    car = ""
    qc = ""
    bc = ""
    age = ""
    name = ""

    def zhengcai(self):
        super().zhengcai()
        print(self.name, "准备好开", self.car, "去厨房", self.qc, "今年", self.age, "岁")

    def chaocai(self):
        super().chaocai()
        print(self.name, "准备", self.bc, "今年", self.age, "岁")


d = tudi()
d.username = "雄安"
d.age = "40"
d.name = "小高"
d.car = "宝马"
d.qc  = "切菜"
d.bc = "拖地"
d.age = "20"
d.zhengcai()
d.chaocai()


#
# c = cook()
# c.username = "雄安"
# # c.age = 15
# c.setnian = "40"
# c.zhengcai()
# c.chaocai()
