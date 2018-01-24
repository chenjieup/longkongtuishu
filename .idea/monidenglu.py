import requests
import re

s = requests.Session()
url_login = 'http://www.lkong.net'
'''
formhash:7d4c2def
referer:/home.php?mod=space&uid=846255
username:文明的读书人
password:chenjie1994612
questionid:0
answer:ffff
'''
formdata = {
    'formhash' : 'fee6ac16',
    'referer' : '/home.php',
    'username': u'文明的读书人',
    'password':'chenjie1994612',
    'questionid':'0',
    'answer':'979082569@qq.com',
    'cookietime':'2592000'
}
cookies = {'cookie':'UM_distinctid=16054dea8d4102-034afb15dfecf6-5a442916-100200-16054dea8d5256; BAIDU_SSP_lcr=https://www.baidu.com/link?url=wkTPRLddxB_0VVeMjZ67eMjp2ZcmL-YmPaXsSVBTT-_d94HhUMcoqS3N0Zr9wwxzleuFEp6d0zjrkxf6wqcNXd6lnWlKPPgmLlD8_d-7CcG&wd=&eqid=a75e0bb90000f7cb000000065a607b89; Hm_lvt_7c968f100abae91ba7d05c5f37881949=1515592296,1516018654,1516111409,1516272531; CNZZDATA1832608=cnzz_eid%3D95585470-1513249364-null%26ntime%3D1516273792; sUJV_ae30_dzsbhey=e6m5IOCU; sUJV_ae30_auth=4872BQ1FlIVFDvrrPZab0aSXRxF6DwNCqm1YPiR%2F32atI%2FcUuinq2ZFrQc%2BlyjvmMgMcse2CBXnMyYSnfGodOrkNidA; sUJV_ae30_lastvisit=1516274634; sUJV_ae30_sid=bKXOKd; sUJV_ae30_onlineusernum=18400; sUJV_ae30_checkpm=1; sUJV_ae30_lastact=1516278778%09home.php%09misc; sUJV_ae30_sendmail=1; Hm_lpvt_7c968f100abae91ba7d05c5f37881949=1516278780'}

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
r = requests.get(url_login,cookies = cookies, headers = header)
print(r.text)