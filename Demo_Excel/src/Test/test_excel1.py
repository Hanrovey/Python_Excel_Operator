
#coding:utf8
'''
Created on 2016年8月12日

@author: chenxihang
'''

import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('test sheet')

worksheet.write(0,0,22222)

workbook.save('test.xls')