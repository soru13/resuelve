#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import time
from time import sleep
import random
import datetime

def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
        yyyy-mm-dd
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
   		pass
    return False

while True:
	user = raw_input("¿Que id tienes?: ")
	start = raw_input("¿Fecha inicio formato(yyyy-mm-dd)?: ")
	finish = raw_input("¿Fecha final formato(yyyy-mm-dd)?: ")
	if validateDateEs(start):
		print ("fecha incorrecta, No hagas trampa :)")
		continue
	if validateDateEs(finish):
		print ("fecha incorrecta, No hagas trampa :)")
		continue
	r = requests.get("http://34.209.24.195/facturas?id=%s&start=%s&finish=%s" % (user,start,finish))
	print r.content


# id ='9a936864-3c10-49a9-b8bd-94bfe26b2163'
# start ='2017-01-01'
# finish ='2017-01-11'
# print r.status_code
# print r.headers
# print r.content


 
