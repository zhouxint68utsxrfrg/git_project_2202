import urllib.request

h={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

req = urllib.request.Request("https://movie.douban.com/top250",headers=h)

r = urllib.request.urlopen(req)

print(r.read().decode())