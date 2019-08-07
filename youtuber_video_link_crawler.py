from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

def filtering(self):
	filter = re.compile('/watch?.*')
	#url_list_proto 내 모든 url 중 유튜버의 콘텐츠만 갖고 오기 위한 정규식을 filter에 저장
	result=filter.search(self)
	#filter의 조건에 맞게 url_list_proto 내 모든 url 필터링하여 result에 저장
	if result != None:
	#해당 조건에 맞지 않으면 none값을 뱉기 때문에 필터링된 값만 추출
		result=result.group()
		#필터링된 값만 갖고 옴
		url_list.append(result)
		#url_list에 저장

if __name__ == '__main__':
	ssl._create_default_https_context = ssl._create_unverified_context
	#ssl 인증서로 유튜브 숨겨진 정보까지 오픈시킴

	url_list_proto=[]
	#정제되지 않은 url_list 받기 위해 선언
	url_list=[]
	#정제한 url_list 받기 위해 선언
	url='https://www.youtube.com/channel/UCT-_4GqC-yLY1xtTHhwY0hA/videos?view=0&sort=dd&flow=grid'
	#크롤링하고 싶은 url 정보 기입

	r=urlopen(url)
	#url에 대한 객체를 r에 돌려줌
	soup=BeautifulSoup(r,"lxml")
	#lxml모듈을 통하여 url에 대한 html데이터 크롤링

	for a_tag in soup.find_all('a', href=True):
	# href가 붙은 a태그를 a_tag에 저장
		url_list_proto.append(a_tag['href'])
		# href 링크 url_list_proto 리스트에 저장
		url_list_proto=list(set(url_list_proto))
		# list 내 중복 제거

	for i in range(len(url_list_proto)):
		filtering(url_list_proto[i])

	for b in range(len(url_list)):
		url_list[b]='https://www.youtube.com'+url_list[b]
		#정제된 url을 url_list 리스트에 저장

	print(url_list)