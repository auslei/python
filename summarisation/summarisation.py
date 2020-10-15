#%%
import nltk
#nltk.download()


# %%
import urllib3
from bs4 import BeautifulSoup

_headers = {        
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Language': "de,en-US;q=0.7,en;q=0.3",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': "google.com",
        'Connection': "keep-alive"
}

url = "https://en.wikipedia.org/wiki/China"

http = urllib3.PoolManager()
r = http.request('GET', url, headers=_headers)

html = BeautifulSoup(r.data, 'html.parser')

text= [e.text for e in html.find_all('p')]

#%%
sample = """the european court of justice ( ecj ) recently ruled in lock v british gas trading ltd that eu law requires a worker 's statutory holiday pay to take commission payments into account - it should not be based solely on basic salary . the case is not over yet , but its outcome could potentially be costly for employers with workers who are entitled to commission . mr lock , an energy salesman for british gas , was paid a basic salary and sales commission on a monthly basis . his sales commission made up around 60 % of his remuneration package . when he took two weeks ' annual leave in december 2012 , he was paid his basic salary and also received commission from previous sales that fell due during that period . lock obviously did not generate new sales while he was on holiday , which meant that in the following period he suffered a reduced income through lack of commission . he brought an employment tribunal claim asserting that this amounted to a breach of the working time regulations 1998 .....deleted rest for readability..."""

# %%
from gensim.summarization.summarizer import summarize


# %%
print(summarize(".".join(text)))

# %%
summarize(sample)

# %%
