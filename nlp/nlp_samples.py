#%% Import and download nltk
import nltk
nltk.download()


#%% craw webpages for data
import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

#%% use beautiful soap
from bs4 import BeautifulSoup

soup = BeautifulSoup(html)
text = soup.get_text(strip = True)
print(text)

#%% Tokenising
tokens = [t for t in text.split()]
print(tokens)

#%% using NLTK tokeniser
tokens = nltk.word_tokenize(text)

# tags are defined explicively in detail below:
#https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b

tagged = nltk.pos_tag(tokens)

from nltk.corpus import treebank
entities = nltk.chunk.ne_chunk(tagged)
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

#%%
%matplotlib inline
from nltk.corpus import stopwords

sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)

#%%
