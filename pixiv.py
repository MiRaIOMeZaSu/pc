import requests
from bs4 import BeautifulSoup
import re
import json
import os
import codecs
from urllib import parse
import threading
import demjson




class pixiv_href(object):
    illustId = []
    pageCount=[]
    search_url = ""
    _return = []

pixiv_href_data=pixiv_href()
downloadfile_data=""
cookies_data=""
threads_number=1

se = requests.session()

def main():
    print("本爬虫由洛水.山岭居室编写(～￣▽￣)～ ")
    data1 = {'device_token':'?','PHPSESSID':'?','DownloadFile':'?'}
    headers = {
       'Referer': 'https://www.pixiv.net',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
       }
    #全局变量修改声明
    global downloadfile_data
    global cookies_data
    global threads
    global threads_number
    if(os.path.isfile("Setting.txt")==True):
        fd=codecs.open('Setting.txt')
        text = fd.read()
        data1 = json.loads(str(text))
        downloadfile=data1['DownloadFile']
        #data1=text_json
    else:
        text_json = json.dumps(data1)
        print (text_json)
    if(data1['device_token']=="?"):
        print("登陆(￣▽￣)／")
        pixiv_id=input("pixiv_id:")
        pixiv_password=input("password:")
        return_to="https://www.pixiv.net"
        post_key_html = se.get("https://accounts.pixiv.net/login", headers=headers)
        post_key_soup = BeautifulSoup(post_key_html.text, 'lxml')
        post_key = post_key_soup.find('input')['value']
        data = {
            'pixiv_id': pixiv_id,
            'password': pixiv_password,
            'return_to': return_to,
            'post_key': post_key
            }
        #print (data)
        data_re=se.post("https://accounts.pixiv.net/api/login?lang=zh", data=data, headers=headers)
        data1['device_token']=data_re.cookies['device_token']
        data1['PHPSESSID']=data_re.cookies['PHPSESSID']
        text_json2 = json.dumps(data1)
        print (text_json2)
        #fd=codecs.open('Setting.txt')
        #fd.write(data1)
        with open("Setting.txt", 'ab') as f: 
            f.write(str(text_json2).encode('utf-8'))     
    #print (data_re.text)
    #data_re_text = json.loads(data_re.text)
    #if(data_re_text['error']['success']['return_to']!='false'):
    if(data1['DownloadFile']=="?"):
        downloadfile=input("DownloadFile:")
        data1['DownloadFile']=downloadfile
        text_json2 = json.dumps(data1)
        with open("Setting.txt", 'w+') as f:
            f.write(str(text_json2))
    print("请输入你要搜索的名字(｡･ω･｡)")
    SearchName=input("Name:")
    cookies_data = dict(device_token=data1['device_token'],PHPSESSID=data1['PHPSESSID'])
    #print(cookies_data)
    dict1 ={'word':SearchName}
    search_url="https://www.pixiv.net/search.php?s_mode=s_tag&"+parse.urlencode(dict1)
    #search_url="https://www.pixiv.net/search.php?s_mode=s_tag&"+parse.urlencode(dict1)+"&order=date_d&p=3"
    search_html = se.get(search_url, headers=headers,cookies=cookies_data)
    search_soup = BeautifulSoup(search_html.text, 'lxml')
    search_input_soup=search_soup.find(id='js-mount-point-search-result-list')
    #print (search_input_soup['data-items'])
    #去除全部带“/“
    #search_input_replace = re.sub('/','',search_input_soup['data-items'])
    #print (search_input_replace)
    data_compile=re.compile("{.*?}",re.S)
    data=re.findall(data_compile,search_input_soup['data-items']) 
    #print (data)
    print("正在解析搜索界面(～￣▽￣)～ ")
    downloadfile_data=downloadfile
    #print (downloadfile_data)
    pixiv_href_data.search_url=search_url
    for rec_data in data:
        text = json.loads(rec_data)
        #print (text)
        #print (text["illustId"])
        #print (text["tags"])
        #print (text["illustTitle"])
        #print (text["bookmarkCount"])
        #pageCount
        if(int(text["bookmarkCount"])>3):
            pixiv_href_data.illustId.append(text["illustId"])
            #pageCount
            pixiv_href_data.pageCount.append(int(text["pageCount"]))
            pixiv_href_data._return.append(0)
        else:
            print("根据书签计数算法已经过滤一个作品(｀・ω・´)作品ID为："+text["illustId"])
    
    print("正在解析作品界面(～￣▽￣)～")
    standII()



#standII
def standII():
    a=len(pixiv_href_data._return)
    for number in range(0,a):
        if(pixiv_href_data._return[number]==0):
            pixiv_href_data._return[number]=1
            if(int(pixiv_href_data.pageCount[number])>1):
                #print (downloadfile_data)
                manga(pixiv_href_data.illustId[number],downloadfile_data)
            else:
                medium(pixiv_href_data.illustId[number],downloadfile_data)


  
            
def manga(illustId,downloadfile):
    headers = {
       'Referer': 'https://www.pixiv.net',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
       }
    print("发现此作品是多图，作品ID：",illustId)
    illust_url="https://www.pixiv.net/member_illust.php?mode=manga&illust_id="+illustId
    headers["Referer"]=pixiv_href_data.search_url
    try:
        member_illust_html = se.get(illust_url, headers=headers,cookies=cookies_data)
    except BaseException as e:
        print("读取网页发生错误(；д；)错误信息为：", e)
        return
    #print (member_illust_html.text)
    headers["Referer"]=illust_url
    item_container_soup = BeautifulSoup(member_illust_html.text, 'lxml')
    manga_image_soup=item_container_soup.find_all('div', attrs={'class', 'item-container'})
    for manga_image_soup_data in manga_image_soup:
        data_src=manga_image_soup_data.find('img')['data-src']
        #print(data_src)
        download(illustId,data_src,headers,downloadfile)

def medium(illustId,downloadfile):
    headers = {
       'Referer': 'https://www.pixiv.net',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
       }
    medium_url="https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+illustId
    headers["Referer"]=medium_url
    #print (illust_url
    illust_url="https://www.pixiv.net/ajax/illust/"+illustId
    try:
        illust_html = se.get(illust_url, headers=headers,cookies=cookies_data)
    except BaseException as e:
        print("读取网页发生错误(；д；)错误信息为：", e)
        return
    #print (member_illust_html.text)
    illust_json = json.loads(illust_html.text)
    #print (illust_json['body']['urls']['original'])
    download(illustId,illust_json['body']['urls']['original'],headers,downloadfile)


def download(illustId,data_src,headers,downloadfile):
    name_compile=re.compile(illustId+'.*',re.S)
    name=re.findall(name_compile,data_src)
    #print(name)
    try:
        html = se.get(data_src, headers=headers)
    except BaseException as e:
        print("下载图片发生错误(；д；)错误信息为：", e)
        return
    img = html.content
    title=downloadfile+'\\'+name[0]
    print("作品ID："+illustId+" 作品下载到："+title)
    with open(title , 'wb') as f:
        f.write(img)


threads = []
for num in range(0,5):
    t1 = threading.Thread(target=standII)
    threads.append(t1)



if(__name__=="__main__"):
    main()
