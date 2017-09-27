# -*- coding: utf-8 -*-


#===========================================================
# открытие в браузере ссылки, соответсвующей случайному треку
# из заданного плейлиста на youtube
#===========================================================

import random
import webbrowser
import requests
from lxml import html

#===========================================================
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

url_prefix = 'https://www.youtube.com'

# playlist url
# Finland
url = 'https://www.youtube.com/playlist?list=PLFgquLnL59anFWmHlKJxf_px-u1TQ9SGy'
#===========================================================

def get_links(url):

    page = requests.get(url)
    webpage = html.fromstring(page.content)
    links_list = webpage.xpath('//a/@href')

    return links_list


def get_playlist_links(links_list):

    playlist_links = [url_prefix + str(item) for item in links_list if (not item is None and str(item).startswith('/watch'))]
    playlist_links = list(dict.fromkeys(playlist_links)) # удаление дубликатов; Python 3.5+

    return playlist_links


def alarm(url):

    links_list = get_links(url)
    playlist_links = get_playlist_links(links_list)
    track_url = random.choice(playlist_links)

    webbrowser.get(chrome_path).open(track_url)

#===========================================================

if __name__ == '__main__':
    alarm(url)
