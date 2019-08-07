from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#ssl로 유튜브 숨겨진 정보까지 오픈시킴
 
url='https://www.youtube.com/watch?v=ja_DflYDg3c&list=PLj6FeOwWCFCqD4DsukLV9Q0MBWf74Bs_j&index=2'
#크롤링하고 싶은 url 정보 기입

r=urlopen(url)
soup=BeautifulSoup(r,"lxml")
print(soup)
s=soup.find("p", id="eow-description").getText()
print(s)