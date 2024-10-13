import urllib.request

import pymysql
from lxml import etree
connection=pymysql.connect(host='localhost',
                          user='root',
                          password='123456',
                          database='mysql',
                          cursorclass=pymysql.cursors.DictCursor)
headers = {
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
def get_first_text(list_of_texts):
   if list_of_texts:
       return list_of_texts[0].strip() if list_of_texts[0] is not None else ""
   return ""
urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i * 25)) for i in range(10)]
with connection:
   for url in urls:
       req = urllib.request.Request(url, headers=headers)
       response = urllib.request.urlopen(req)
       html_doc = response.read().decode('utf-8')
       html = etree.HTML(html_doc)
       list = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
       for index, li in enumerate(list, start=1):
           # 图片
           img = get_first_text(li.xpath('div/div[1]/a/img/@src'))
           # 标题
           title = get_first_text(li.xpath('div/div[2]/div[1]/a/span[1]/text()'))
           # 网址
           src = get_first_text(li.xpath('div/div[2]/div[1]/a/@href'))
           # 导演
           director = get_first_text(li.xpath('div/div[2]/div[2]/p[1]/text()'))
           # 类型
           type = get_first_text(li.xpath('div/div[2]/div[2]/p[1]/text()[2]'))
           # 评价
           comment = get_first_text(li.xpath('div/div[2]/div[2]/div/span[4]/text()'))
           # 引用
           quote=get_first_text(li.xpath('div/div[2]/div[2]/p[2]/span/text()'))
           with connection.cursor() as cursor:
               sql = "INSERT INTO douban250 (img, title, src, director, type, comment, quote)" \
                     "VALUES(%s,%s,%s,%s,%s,%s,%s)"

               cursor.execute(sql,(img, title, src, director, type, comment, quote))
   connection.commit()