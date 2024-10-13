import urllib.request

h={

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
   }
req=urllib.request.Request("https://movie.douban.com/top250",headers=h)

proxies={"http":"117.71.155.47:8089"}
proxy_handler=urllib.request.ProxyHandler()
opener=urllib.request.build_opener(proxy_handler)


r=opener.open(req)
#r=urllib.request.urlopen(req)

print(r.read().decode())