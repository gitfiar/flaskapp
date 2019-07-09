##!/bin/python 
#coding:utf-8
import urllib
import urllib2
import pprint
import json
import sys
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex  
import random

reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

class Sms(object):
	def __init__(self,toNumber):
            self.appId = '102006' 
            self.apiUrl = 'http://sms_developer.zhenzikj.com' 
            self.appSecret = 'MzQxODBjMTItNWUxOS00MzM3LWE2ZTItZTcxNDk2NjllMDFj'
            self.toNumber=toNumber
            self.messageId=''
            self.message=u"请确保你本人操作，你的验证码是:"
	def send(self, messageId=''):
                mId = messageId if messageId else self.messageId 
		data = {
                    'appId': self.appId,
		    'appSecret': self.appSecret,
		    'message': self.message,
		    'number': self.toNumber,
		    'messageId':mId
		}
		data = urllib.urlencode(data);
		req = urllib2.Request(self.apiUrl+'/sms/send.do', data);
		res_data = urllib2.urlopen(req);
		res = res_data.read();
                self.messageId=mId
                result = json.loads(res)
		return result;


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
        def getHisCode(self,messid):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret,
                    'messageId':messid
		}
		data = urllib.urlencode(data);
		req = urllib2.Request(self.apiUrl+'/smslog/findSmsByMessageId.do', data);
		res_data = urllib2.urlopen(req);
		res = res_data.read();
                j = json.loads(res)
                smsCode = j['data']['message'].split(':',1)[1]
                return int(smsCode);
        def randomCode(self):
                alist = ""
                for i in range(6):
                    j = random.randint(0, 9)
                    alist = alist + str(j)
                mId=int(self.toNumber)+int(alist)
                self.messageId=mId
                self.message= self.message+ alist
                return self
#  n='188244'
#  sms = Sms(n)
#  code=sms.randomCode()
#  res = code.send()
#  print res
#  result= "yes" if res['code']==0  else "no"
#  print result
#  code.send('aasx')
#  print code.messageId
#  #re=sms.send(mess,mId)
#  pprint.pprint(code.message)
#  re=code.findmess('44445')
#  j=json.loads(re)
#  pprint.pprint(j['data']['message'])
#  print j['data']['message'].split(':',1)[1]
