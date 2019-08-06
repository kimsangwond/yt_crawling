import requests
import json
from bs4 import BeautifulSoup
import sys
import io
sys.setrecursionlimit(10**6)

print('Blues')
print('Classical')
print('Country')
print('Electronic')
print('Experimental')
print('Folk')
print('Hip-Hop')
print('Instrumental')
print('International')
print('Jazz')
print('novelty')
print('Old-Time__Historic')
print('Pop')
print('Rock')
print('Soul-RB')
print('Spoken')

genre=raw_input('input genre: ')

def fma_Crawling(html, page):
	temp_dict = {}
	div_list = html.find_all('div', {'class': 'play-item'})
	artist_list = []
	track_list = []
	album_list = []
	genre_list = []
	i=(page-1)*200-1

	for div in div_list :
		i=i+1
		artist = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-artist'}).text
		track = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-track'}).text
		album = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-album'}).text
		genre = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-genre'}).text
		temp_dict[str(i+1)]={'artist':str(artist.encode('utf-8')), 'track':str(track.encode('utf-8')), 'album':str(album.encode('utf-8')), 'genre':str(genre.encode('utf-8'))}

	return temp_dict

def toJson(fma_dict):

    with io.open('{}_chart.json'.format(genre), 'w', encoding='utf-8') as file :
        json.dump(fma_dict, file, ensure_ascii=False, indent='\t')

fma_dict={}

req1 = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page=1&per_page=200/'.format(genre))

source1 = req1.text
html2 = BeautifulSoup(source1, 'lxml')
final_page2=html2.select('a[href^="https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page="]'.format(genre))
print(final_page2)
final_page=final_page2[6].text
print(final_page)
final_page=int(final_page)

final_song2=html2.find('div', {'class': 'pagination-full'}).find_all("b")
final_song=final_song2[2].text
final_song=int(final_song)

for page in range(1,final_page+1):
	req = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page={}&per_page=200'.format(genre, page))
	source = req.text
	html = BeautifulSoup(source, 'lxml')
	fma_dict = dict(fma_dict, **fma_Crawling(html,page))
	print(fma_dict)

toJson(fma_dict)