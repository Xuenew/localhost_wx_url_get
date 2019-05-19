#Author:xue yi yang
#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAIkhQicIDwuAPU', 'TatinbuNNC4MMD9lCLBQPUs1i3WVgF', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "18188108851")
request.add_query_param('SignName', "友借友还")
request.add_query_param('TemplateCode', "SMS_165414732")
request.add_query_param('TemplateParam', "{\"code\":\"8851\"}")

response = client.do_action(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
