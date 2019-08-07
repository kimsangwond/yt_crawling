from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

def filtering(self):
	filter = re.compile('/watch?.*') # 한글과 띄어쓰기를 제외한 모든 글자
	# hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
	result=filter.search(self)
	#result = re.sub(str(self), filter) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
	if result != None:
		result=result.group()
		lists.append(result)

if __name__ == '__main__':
	ssl._create_default_https_context = ssl._create_unverified_context
	#ssl 인증서로 유튜브 숨겨진 정보까지 오픈시킴

	url_list=[]
	lists=[]

	url='https://www.youtube.com/channel/UCT-_4GqC-yLY1xtTHhwY0hA/videos?view=0&sort=dd&flow=grid'
	#크롤링하고 싶은 url 정보 기입

	r=urlopen(url)
	soup=BeautifulSoup(r,"lxml")
#classes=soup.find_all("a", {'class': 'yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2'})
#all_video_url=soup.find_all("a", href=True)
#print(all_video_url)

	for a in soup.find_all('a', href=True):
		url_list.append(a['href'])

	for i in range(100):
		filtering(url_list[i])

	print(lists)

#print(url_list)