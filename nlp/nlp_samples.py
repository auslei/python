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
from nltk import word_tokenize, sent_tokenize
tokens = nltk.word_tokenize(text)
s_tokens = sent_tokenize(text)

# tags are defined explicively in detail below:
#https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b

from nltk.stem import PorterStemmer

from nltk.corpus import wordnet

tagged = nltk.pos_tag(tokens)
st = PorterStemmer()

#get nouns from the tokens with pos tags, only english words
nouns = [x for x, y in tagged if y in ['NNP', 'NN', 'NNS'] and wordnet.synsets(x)]
stemmed = [st.stem(x) for x in nouns]

freq = nltk.FreqDist(stemmed)
#%%

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

#%%word cloud
from wordcloud import WordCloud
from matplotlib import pyplot as plt
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(stemmed))
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()