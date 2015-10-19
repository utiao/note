#coding:utf8
__author__ = 'adair'
import os

ip='localhost'
port=8000
os.system('python3.4 manage.py runserver {0}:{1}'.format(ip,port))