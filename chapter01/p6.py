import requests


headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}

proxies={
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890'
}

data={'username':'zhouxin',
      'passwd':'123456',
      'authcode':'CJUE',  #为什么输入验证码还是错误或过期
      'toUrl':'',
      'app':'accountr.aja_login'}

r=requests.post("http://www.nowapi.com/index.php?ajax=1",headers=headers,proxies=proxies,data=data)
print(r.text)