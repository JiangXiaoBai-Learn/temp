# -*- coding: GBK -*-
# Author：Kevin姜林斌

import os
from selenium import webdriver
import sys


########################################################################################################################
#当前模块：SomoCS公共方法集                                                                                            #
#Created By:   Kvin Jiang LinBin                                                                                       #
#Updated By:   Kvin Jiang LinBin                                                                                       #
#Update Date:  2014-12-01                                                                                              #
#Personal Email:  jianglinbin_zzu@163.com                                                                              #
#Company:MD-Technologies HangZhou                                                                                      #
#Business System:Mei System                                                                                            #
#Version:PageObject V1.0                                                                                               #
########################################################################################################################

"""全局变量--驱动为chrome"""
ChromeDriver=webdriver.Chrome()

"""全局变量--登陆界面的URL"""
LoginUrl=u'http://192.168.10.206/somoStorage'

"""当前工作路径"""
parentdir=os.path.split(os.getcwd())[0]

"""日志信息存放位置"""
loginfo_file_path=str(os.path.split(parentdir)[0])+'\\Log'

"""截图存放位置"""
screens_file_path=str(os.path.split(parentdir)[0])+'\\PageScreen\\'



