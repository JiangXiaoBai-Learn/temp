# -*- coding: GBK -*-
# Author��Kevin���ֱ�

import os
from selenium import webdriver
import sys


########################################################################################################################
#��ǰģ�飺SomoCS����������                                                                                            #
#Created By:   Kvin Jiang LinBin                                                                                       #
#Updated By:   Kvin Jiang LinBin                                                                                       #
#Update Date:  2014-12-01                                                                                              #
#Personal Email:  jianglinbin_zzu@163.com                                                                              #
#Company:MD-Technologies HangZhou                                                                                      #
#Business System:Mei System                                                                                            #
#Version:PageObject V1.0                                                                                               #
########################################################################################################################

"""ȫ�ֱ���--����Ϊchrome"""
ChromeDriver=webdriver.Chrome()

"""ȫ�ֱ���--��½�����URL"""
LoginUrl=u'http://192.168.10.206/somoStorage'

"""��ǰ����·��"""
parentdir=os.path.split(os.getcwd())[0]

"""��־��Ϣ���λ��"""
loginfo_file_path=str(os.path.split(parentdir)[0])+'\\Log'

"""��ͼ���λ��"""
screens_file_path=str(os.path.split(parentdir)[0])+'\\PageScreen\\'



