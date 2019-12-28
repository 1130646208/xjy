import urllib.request
import random
url = 'https://www.whatismyip.com/'
iplist = ['1.193.246.69:9999','49.77.209.196:9999','123.169.165.255:9999']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0')]


urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
