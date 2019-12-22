#%% Setup
import urllib3
from bs4 import BeautifulSoup
from datetime import datetime

_base_url = "https://www.news.com.au/"
_headers = {        
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Language': "de,en-US;q=0.7,en;q=0.3",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': _base_url,
        'Connection': "keep-alive"
}


# get content of an url
def get_content(url):
    #%% Get Headline
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=_headers)

    if r.status == 200:
        html = BeautifulSoup(r.data, 'html.parser')
    else:
        print(r.status)
        html = None
    return html

#%% get all the new in the top news
def read_news(_base_url):
    import re
    regex = re.compile("story-block.*")    

    stories = {"timestamp": [], "headline": [], "link": [], "content": []}

    for story in  get_content(_base_url).find_all('div', {'class': regex}):
        heading = story.find('h4', {'class': 'heading'})
        if heading:
            a = heading.find('a')
            headline = a.text
            link = a.get('href')
            content = " ".join([p.text for p in get_content(link).find_all('p')])
            stories['headline'].append(headline)
            stories['link'].append(link)
            stories['content'].append(content)
            ts = story.find('span', {'class': 'datestamp'})
            if ts:
                stories['timestamp'].append(f"{ts.txt} {ts.find('span', {'class': 'time'}).text}")
            else:
                stories['timestamp'].append(datetime.now().strftime("Last updated %B %d, %Y %H:%M:%S AEDT"))
            

    return pd.DataFrame(stories)

#%%
df = read_news(_base_url)