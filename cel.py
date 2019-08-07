from selenium import webdriver
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



driver = webdriver.Chrome('/Users/sangwon/workspace/youtube_crawling/chromedriver')
driver.implicitly_wait(3)
# url에 접근

driver.get('https://www.youtube.com/channel/UCT-_4GqC-yLY1xtTHhwY0hA/videos?view=0&sort=dd&flow=grid')
# 들어가고자 하는 url 입력

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('#video-title > href')

#//*[@id="video-title"]

#video-title

#document.querySelector("#video-title")

for n in notices:
    print(n.text.strip())