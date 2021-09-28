
import xlrd
wb = xlrd.open_workbook('111.xls')

from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank

sheet1 = wb.sheet_by_index(0)
data_addUser = sheet1.row_values(1, sheet1.nrows)


@ddt
class TestAdduser(TestCase):

    @data(*data_addUser)
    @unpack
    def testAdd(self, account, username, password, country, province, street, door):
        b = bank()
        result = b.adduser(account, username, password, country, province, street, door)
        self.assertEqual(b, result)

sheet2 = wb.sheet_by_index(1)
data_savemoney = sheet2.row_values(1, sheet2.nrows)

@ddt
class TestSave(TestCase):

    @data(*data_savemoney)
    @unpack
    def testSave(self, account, money):
        b = bank()
        result = b.saving(account, money)
        self.assertEqual(b, result)

sheet3 = wb.sheet_by_index(2)
data_getmoney = sheet3.row_values(1, sheet3.nrows)

@ddt
class TestGetmoney(TestCase):

    @data(*data_getmoney)
    @unpack
    def testGet(self, account, money):
        b = bank()
        result = b.withdrawing(account, money)
        self.assertEqual(b, result)

sheet4 = wb.sheet_by_index(3)
data_trans = sheet4.row_values(1, sheet4.nrows)

@ddt
class TestTrans(TestCase):

    @data(*data_trans)
    @unpack
    def testTrans(self, faccount, taccount, money):
        b = bank()
        result = b.transfer(faccount, taccount, money)
        self.assertEqual(b, result)

sheet5 = wb.sheet_by_index(4)
data_search = sheet4.row_values(1, sheet5.nrows)

@ddt
class TestSearch(TestCase):

    @data(*data_search)
    @unpack
    def testSearch(self, account):
        b = bank()
        result = b.query(account)
        self.assertEqual(b, result)