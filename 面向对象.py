class sb:
    h = 0
    l = 0
    color = ""
    def water(self,color):
        print(color,"的杯子在盛红酒")

    def wc(self,color,altitude ):
        print(color,"杯子盛水，装了",altitude,"升！")

c = sb()
c.water("绿色")
c.wc("绿色",1)




class legion:
    _pm = 0
    _money = 0
    _cpu = ""
    _nc = ""
    _dj = ""
    def setsum(self,money):
        self._money=money

    def getsum(self):
        return self._money
    def setNC(self,nc):
        if nc > 1000 or nc<0:
            print("没有您要找的型号，禁止访问")
        else:
            self._nc = nc
    def setDJ(self,dj):
        if dj > 200 or dj<0:
            print("没有您要找的型号")
        else:
            self._dj = dj




    def DZ(self,yyds):
        print(self._money,"$","电脑打字，内容是",yyds)
    def DYX(self,name,wzry):
        print(self._nc,"g","打游戏，内容是",wzry)
    def KSP(self,yellow):
        print(self._dj,"min待机","看的内容为",yellow)
    def zhanshi(self):
        print("此电脑为legion",self._money,"内存为",self._nc,"待机时长",self._dj)










a = legion()
# a.money = 50000
a.setsum(50000)
# a.nc = 500
a.setNC(500)
# a.dj = 180
a.setDJ(180)
a.DZ("yyds")
a.DYX(10,"wzry")
a.KSP("yellow")
a.zhanshi()




