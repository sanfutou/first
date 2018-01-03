import requests
from bs4 import BeautifulSoup

url1 = 'http://www.pm25x.com/'  #获得主页面链接
html = requests.get(url1)  #抓取主页面数据
sp1 = BeautifulSoup(html.text, 'html.parser')  #把抓取的数据进行解析

city = sp1.find("a",{"title":"上海PM2.5查询"})  #从解析结果中找出title属性值为"北京PM2.5"的标签
#print(city)
citylink=city.get("href")  #从找到的标签中取href属性值
#print(citylink)
url2=url1+citylink  #生成二级页面完整的链接地址
#print(url2)

html2=requests.get(url2)   #抓取二级页面数据
sp2=BeautifulSoup(html2.text,"html.parser")   #二级页面数据解析
#print(sp2)
data1=sp2.select(".aqivalue")  #通过类名aqivalue抓取包含北京市pm2.5数值的标签
pm25=data1[0].text   #获取标签中的pm2.5数据
print("上海市此时的PM2.5值为："+pm25) #显示pm2.5值
