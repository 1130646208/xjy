import urllib.request
import os




def get_page(url):
    '''抓取网页地址(从当前url中的'下一页'开始)
    返回一个url'''
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page')
    a = html.find('jandan.net/ooxx/',a)
    b = html.find('#comments',a) + 9
    
    return 'http://' + html[a:b]
    

def find_imgs(url):
    '''获取当前url中的jpg源地址,返回一个列表,包含了当前页面的几乎所有jpg'''
    img_addrs = []
    html = url_open(url).decode('utf-8')
    a = 0
    b = 0
    while True:
        a = html.find('li id="comment',a)
        if a == -1:
            break
        a = html.find('img src=',a) + 11
        if a == 10:
            break
        b = html.find('.jpg',a, a + 255) + 4
        if b == 3:
            break
        img_addrs.append(html[a:b])
        a = b
    print(img_addrs)
    return img_addrs


    
    

def save_imgs(folder, img_addrs):
    '''将图像保存到文件夹'''
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open('http://' + each)
            f.write(img)

def url_open(url):
    '''打开url,返回未解码的html'''
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0')
    '''
    如需代理则uncomment
    proxies = []
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    
    '''
    response = urllib.request.urlopen(req)
    html = response.read()

    return html



def download_mm(folder='ooxx',pages = 10):
    
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'http://jandan.net/ooxx/'
    next_page = get_page(url)
    for page in range(pages):
        print(next_page)
        save_imgs(folder, find_imgs(next_page))
        next_page = get_page(next_page)
    

        



if __name__ == '__main__' :
    download_mm('ooxx2',pages=1)
