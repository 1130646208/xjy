import urllib.request
import urllib.parse
import json


#the youdao translate site
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
origin_text = input('请输入要翻译的文本:')
#header
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'

#the data sheet
data = {}
data['i'] = origin_text
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
#encode to url data
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
result = json.loads(html)
print('翻译结果是:',result['translateResult'][0][0]['tgt'])



