# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:20:21 2019

@author: Sai Charan Reddy
"""

import numpy as np
import pandas as pd

df = pd.read_json('../data/raw_keywords.json')
df = df.drop(df[df.error.isna() == False].index, axis=0)
df = df.drop(columns=['error'], axis=1)

from itertools import chain

org_results_all = list(chain(*df.organic_results))
df_org = pd.Series(org_results_all)
df_ind = df_org.apply(lambda x: 'snippet' in x.keys())
df_org = df_org[df_ind]

df_texts = df_org.apply(lambda x: x['title'] + ' ' + x['snippet'])
df_texts[0]

all_texts = ' '.join(df_texts)
all_texts = all_texts # [:5000000]

import spacy
import en_core_web_lg
nlp = en_core_web_lg.load(disable=['ner'])

nlp.max_length = 10366465
doc = nlp(all_texts)

a = [chunk for chunk in doc.noun_chunks][:100]

def token_clean_up(token):
    """ token cleanup. Return clean token or None. """
    removal=['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE']
    if token.is_stop == False and token.is_alpha and len(token)>3 and token.pos_ not in removal:
        return token.lower_
    else:
        return ""

from collections import Counter

# all tokens that arent stop words or punctuations
words = [token_clean_up(token) for token in doc]

# noun tokens that arent stop words or punctuations
nouns = [token_clean_up(token) for token in doc if token.pos_ == "NOUN"]

# noun chunks 
noun_chunks = [chunk for chunk in doc.noun_chunks]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(100)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(100)   

noun_chunk_freq = Counter(noun_chunks)
common_chunks = noun_chunk_freq.most_common(100)

common_chunks[:10]

', '.join([i for i,z in common_nouns])

', '.join([i for i,z in common_words])
