# import xlrd
#
# # 工作簿
# wb = xlrd.open_workbook(filename=r"D:\任务py\day07【mysql工具类与excel读取】\2020年每个月的销售情况.xlsx")
#
# # 确定选项卡
# sheet = wb.sheet_by_name("1月")
# # 获取有多少行多少列
# rows = sheet.nrows
# cols = sheet.ncols
#
# print(rows, "  ", cols)
# for i in range(0, cols):
#     print(sheet.col_values(i))
# for i in range(0, rows):
#     data = sheet.row_values(i)
#     print(data)
#
# sum = 0
#
# for i in range(1, rows):
#     data = sheet.row_values(i)
#     sum = sum + data[2] * data[4]
#
# print("1月销售额:", round(sum))

#全年的销售总额
import xlrd
wb = xlrd.open_workbook(filename=r"D:\任务py\day07【mysql工具类与excel读取】\2020年每个月的销售情况.xlsx")
month = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
sum2 = 0
for a in range(0,12):
    sheet = wb.sheet_by_name(month[a])
    rows = sheet.nrows
    sum1 = 0
    for i in range(1, rows):
        data = sheet.row_values(i)
        sum1 = sum1 + data[2] * data[4]
    sum2 = sum2 + sum1
print("12个月总的销售额", round(sum2),"￥")
print("-------------------------------")

 #每件衣服的销售总量
macary = {}
import xlrd
wb = xlrd.open_workbook(filename=r"D:\任务py\day07【mysql工具类与excel读取】\2020年每个月的销售情况.xlsx")
month = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
#cols = sheet.ncols
sum5 = 0
for i in range(0,12):
    sheet = wb.sheet_by_name(month[i])
    rows = sheet.nrows
    for i in range(1,rows):
        data = sheet.row_values(i)
        sum5 = sum5 + data[4]
print("总销售量为:",round(sum5),"件")
print("---------------------------")





#每件衣服的占比为
for i in range (0,12):
    st = wb.sheet_by_name(month[i])
    rows = st.nrows
    for i in range(1,rows):
        data = st.row_values(i)
        if data[1] in macary:
            macary[data[1]] = macary[data[1]]+data[4]
        else:
            macary[data[1]] = data[4]
print("每种衣服销售:",macary,"￥")
print("----------------")
print("最畅销的衣服：")
max = max(macary.values())
for key,values in macary.items():
    if values==max:
        print(key,round(max),"￥")
        print("---------------------")
print("最不畅销的衣服：")
min = min(macary.values())
for key,values in macary.items():
    if values==min:
        print(key,round(min),"￥")
        print("------------------")


print("每件衣服的占比为：")
for i in macary:
    print(i,round(macary[i]/sum5*100,1),"%")
print("--------------")

#每件衣服销售额占比：
for a in range(0, 12):
    sheet = wb.sheet_by_name(month[a])
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        sheet.row_values(i)
        if data[1] in macary:
           macary[data[1]] = macary[data[1]] + data[2] * data[4]
        else:
            data=macary[data[1]] = data[2] * data[4]
print("每种衣服一年的销售额为：",macary)


print("每件衣服销售额占比：")
for i in macary:
    print(i,round(macary[i]/sum2*100,1),"%")
print("-------------------------")

#每个季度最畅销的



















