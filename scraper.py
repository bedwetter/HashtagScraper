import requests
from bs4 import BeautifulSoup



url = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23'
search_tag = str(input('Enter tag you would like to search: '))

if '#' in search_tag:
    search_tag = search_tag.strip('#')


r = requests.get(url + search_tag)
j = r.json()
j_hash = j['hashtags']

for info in j_hash:
    name = info['hashtag']['name']
    print('#' + name)


if __name__ == "__main__":
    run = get_tags()
