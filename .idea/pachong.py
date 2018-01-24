import requests
from bs4 import BeautifulSoup
import re
import csv

url = ['http://www.lkong.net/forum-60-%s.html' %i for i in range(100,341)]

def get_pageurl(url):
    item = []
    tup = ()
    cookies = {'cookie':'UM_distinctid=16054dea8d4102-034afb15dfecf6-5a442916-100200-16054dea8d5256; BAIDU_SSP_lcr=https://www.baidu.com/link?url=wkTPRLddxB_0VVeMjZ67eMjp2ZcmL-YmPaXsSVBTT-_d94HhUMcoqS3N0Zr9wwxzleuFEp6d0zjrkxf6wqcNXd6lnWlKPPgmLlD8_d-7CcG&wd=&eqid=a75e0bb90000f7cb000000065a607b89; Hm_lvt_7c968f100abae91ba7d05c5f37881949=1515592296,1516018654,1516111409,1516272531; CNZZDATA1832608=cnzz_eid%3D95585470-1513249364-null%26ntime%3D1516273792; sUJV_ae30_dzsbhey=e6m5IOCU; sUJV_ae30_auth=4872BQ1FlIVFDvrrPZab0aSXRxF6DwNCqm1YPiR%2F32atI%2FcUuinq2ZFrQc%2BlyjvmMgMcse2CBXnMyYSnfGodOrkNidA; sUJV_ae30_lastvisit=1516274634; sUJV_ae30_sid=bKXOKd; sUJV_ae30_onlineusernum=18400; sUJV_ae30_checkpm=1; sUJV_ae30_lastact=1516278778%09home.php%09misc; sUJV_ae30_sendmail=1; Hm_lpvt_7c968f100abae91ba7d05c5f37881949=1516278780'}
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    response = requests.get(url,cookies = cookies,timeout = 3,headers = header)
    html = BeautifulSoup(response.text,"lxml")
    content = html.findAll("tbody",attrs={"id":re.compile(r"normalthread.*?")})
    for i in content:
        page_url =i.find("a",{"class":"xst"})['href']
        title = i.find("a",{"class":"xst"}).get_text()
        author = i.find("cite").get_text().strip()
        data = i.find("td",{"class":"by"}).find("em").get_text()
        heat = i.find("a",{"class":"xi2"}).get_text()
        if i.span is not None:
            page_num = i.span.findAll("a")[-1].get_text()
        else:
            page_num = 1
        tup =(page_url,title,page_num,author,data,heat)
        item.append(tup)
    return item

def pageparse(url):
    cookies = {'cookie':'UM_distinctid=16054dea8d4102-034afb15dfecf6-5a442916-100200-16054dea8d5256; BAIDU_SSP_lcr=https://www.baidu.com/link?url=wkTPRLddxB_0VVeMjZ67eMjp2ZcmL-YmPaXsSVBTT-_d94HhUMcoqS3N0Zr9wwxzleuFEp6d0zjrkxf6wqcNXd6lnWlKPPgmLlD8_d-7CcG&wd=&eqid=a75e0bb90000f7cb000000065a607b89; Hm_lvt_7c968f100abae91ba7d05c5f37881949=1515592296,1516018654,1516111409,1516272531; CNZZDATA1832608=cnzz_eid%3D95585470-1513249364-null%26ntime%3D1516273792; sUJV_ae30_dzsbhey=e6m5IOCU; sUJV_ae30_auth=4872BQ1FlIVFDvrrPZab0aSXRxF6DwNCqm1YPiR%2F32atI%2FcUuinq2ZFrQc%2BlyjvmMgMcse2CBXnMyYSnfGodOrkNidA; sUJV_ae30_lastvisit=1516274634; sUJV_ae30_sid=bKXOKd; sUJV_ae30_onlineusernum=18400; sUJV_ae30_checkpm=1; sUJV_ae30_lastact=1516278778%09home.php%09misc; sUJV_ae30_sendmail=1; Hm_lpvt_7c968f100abae91ba7d05c5f37881949=1516278780'}
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    response = requests.get(url,cookies = cookies,timeout = 3,headers = header)
    html = BeautifulSoup(response.text,"lxml")
    contents = html.findAll("div",{"class","t_fsz"})
    name = re.compile('《(.*?)》',re.S)
    bookname = re.findall(name,str(contents))
    return bookname

# cscfile = open('debug.csv','a')
# writer = csv.writer(cscfile)
# writer.writerow(['title','author','data','heat','name'])

for i in url:
    try:
        page_item = get_pageurl(i)
        for page in page_item:
            print("爬取标题为{}的页面,共{}页,发帖人为{},发帖日期为{},回复数为{}".format(page[1],page[2],page[3],page[4],page[5]))
            bookname = []
            a=page[0].split('-')
            for i in range(1,int(page[2])+1):
                print("爬取第{}页".format(i))
                url = a[0]+'-'+a[1]+'-'+str(i)+'-'+a[3]
                print(url)
                name = pageparse(url)
                bookname.extend(name)
                bookname = list(set(bookname))
                book =','.join(bookname).strip('"')

            cscfile = open('he.csv','a')
            try:
                writer = csv.writer(cscfile)
                writer.writerow([page[1],page[3],page[4],page[5],book])
            except:
                print("写入错误")
            finally:
                pass
    except:
        print('error')
    finally:
        pass
cscfile.close()
