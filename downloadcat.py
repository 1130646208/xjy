import urllib.request
response = urllib.request.urlopen('http://placekitten.com/g/800/800')
cat_img = response.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
    

print(response.geturl())
print(response.info())


"""
或者
req = urllib.request.Request('http://')
response = urllib.request.urlopen(req)

"""
