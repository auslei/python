#%% 
import nltk
from nltk.tokenize import word_tokenize

# %%
text = "who bunch of useless text"

# %%
def tokenize(text):
    return word_tokenize(text)

tokens = tokenize(text)

# %%
