#/usr/bin/python
#coding:utf-8
from twilio.rest import Client 
 
account_sid = 'AC657cc7bb303dfa17d990036c48876c61' 
auth_token = 'f47f1a90739ca01389fa70cf693390ab' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+16309485133',        
                              to='+8613240510023',
                              body='验证码是212313'
                          ) 
 
print(message.sid)

