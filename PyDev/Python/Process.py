#!/usr/bin/python
#-*- coding: utf-8 -*-

import psutil

print (psutil.cpu_percent())             #cpu사용량
print (psutil.virtual_memory().percent)  #메모리 사용량
print (psutil.disk_usage('/').percent)   #디스크 사용량
