# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   process_excel.py
 
@Time    :   2020/9/7 8:50 下午
 
@Desc    :
 
"""

import xlrd


def excel():

    out = open('result.txt', 'a')
    wb = xlrd.open_workbook('/Data/xiaobensuan/Codes/HelloWorld/data/葡萄酒-智能知识问答.xlsx')  # 打开Excel文件
    sheet = wb.sheet_by_name('智能知识库问答型导入')  # 通过excel表格名称(rank)获取工作表

    for a in range(1, sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
        dat = []  # 创建空list
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        question = cells[0]
        anwser = cells[1]
        dat.append(question)
        sim_ques = cells[3].split('\n')
        dat = dat + sim_ques
        question_str = '&&'.join(dat)
        print(question_str)
        out.write('【问题】' + question_str + '\n' + anwser + '\n')
        out.write('\n')


a = excel()  # 返回整个函数的值
