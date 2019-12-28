import urllib.request
import json
import pickle


pickle_file = open('city_data.pkl','rb')
city = pickle.load(pickle_file)
password = input('请输入城市:')
name1=city[password]
File1=urllib.request.urlopen('http://www.weather.com.cn/data/sk/'+name1+'.html')
weatherHTML=File1.read().decode('utf-8')
weatherJSON = json.JSONDecoder().decode(weatherHTML)
weatherInfo = weatherJSON['weatherinfo']


print('时间:',weatherInfo['time'])
print('城市:',weatherInfo['city'])
print('温度:',weatherInfo['temp'],'℃')
print('风向:',weatherInfo['WD'])
print('风速:',weatherInfo['WS'])
print('湿度:',weatherInfo['SD'])
print('气压:',weatherInfo['AP'])
print('?',weatherInfo['WSE'])
print('?:',weatherInfo['sm'])
