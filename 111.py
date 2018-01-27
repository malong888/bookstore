#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-26 下午4:12
# @Author  : Michael
# @Site    : 
# @File    : 111.py
# @Software: PyCharm

import time


def fun(func):
	def wroop(a):
		start_time = time.time()
		func(a)
		end_time = time.time()
		data_time = end_time - start_time
		print(data_time)

	return wroop


@fun
def func(a):
	print('hello')
	time.sleep(1)
func('world')
