##!/bin/python 
#coding:utf-8 -*- coding: utf-8 -*-
import urllib
import urllib2
import pprint
import json
import sys
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex  


reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf')

class Sms(object):
	def __init__(self,toNumber):
            self.appId = '102006' 
            self.apiUrl = 'http://sms_developer.zhenzikj.com' 
            self.appSecret = 'MzQxODBjMTItNWUxOS00MzM3LWE2ZTItZTcxNDk2NjllMDFj'
            self.toNumber=toNumber
            self.messageId=''

	def send(self, number, message, messageId=''):
		data = {
    	    'appId': self.appId,
		    'appSecret': self.appSecret,
		    'message': message,
		    'number': number,
		    'messageId': messageId
		}
		data = urllib.urlencode(data);
		req = urllib2.Request(self.apiUrl+'/sms/send.do', data);
		res_data = urllib2.urlopen(req);
		res = res_data.read();
		return res;


	def balance(self):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret
		}
		data = urllib.urlencode(data);
		req = urllib2.Request(self.apiUrl+'/account/balance.do', data);
		res_data = urllib2.urlopen(req);
		res = res_data.read();
		return res;
        def findmess(self,messid):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret,
                    'messageId':messid
		}
		data = urllib.urlencode(data);
		req = urllib2.Request(self.apiUrl+'/smslog/findSmsByMessageId.do', data);
		res_data = urllib2.urlopen(req);
		res = res_data.read();
		return res;
      
clien =Sms('13240510023')
aa= des_encrypt('sasd')
print aa
ree=clien.findmess('7724a1')
print(clien.messageId)
a= ree.decode('unicode_escape')  
b= json.loads(ree)
print(b[u'data']) 
