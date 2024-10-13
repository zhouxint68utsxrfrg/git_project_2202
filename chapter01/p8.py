import requests
from bs4 import BeautifulSoup
import ddddocr

headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}

proxies={
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890'
}
#请求登陆界面
s=requests.session()
login=s.get('https://www.nowapi.com/?app=account.login',headers=headers,proxies=proxies)
print(login.text)

#解析页面获得验证码
soup=BeautifulSoup(login.text,'html.parser')
image_url=soup.find_all(id='authCodeImg')[0]['src']

#把验证码存储为图片
rep_code=s.get(str(image_url),headers=headers,proxies=proxies)
image_code=rep_code.content
with open('../zx.jpg', 'wb')as f:
    f.write(image_code)

#破解验证码
ocr=ddddocr.DdddOcr()
image=open('../zx.jpg', 'rb').read()
result=ocr.classification(image)
print(result)

#通过验证码进行登录


data={'username':'syl9617016',
      'passwd':'syl123321',
      'authcode':'GFUQ',  #为什么输入验证码还是错误或过期
      'toUrl':'',
      'app':'accountr.aja_login'}

r=requests.post("http://www.nowapi.com/index.php?ajax=1",headers=headers,proxies=proxies,data=data)
print(r.text)