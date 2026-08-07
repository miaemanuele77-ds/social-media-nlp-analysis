#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:19:32 2026

@author: miaemanuele
"""


import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('tagsets_json')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

post_text = ''' Big link up tonight 🔥 
                8:30 @ Broadgate by the statue 
                bring fireworks 😂 don’t be soft 
                cov uni lot better show up 
                #CovTakeover #LinkUp #CityCentre '''



# Following the NLP pipeline:
    
# -------------------------
# Sentence segmentation
# -------------------------    
from nltk.tokenize import sent_tokenize
post_sent = sent_tokenize(post_text) 
print(post_sent)

for sentence in post_sent:
 print(sentence)


# -------------------------
# Tokenisation
# -------------------------
from nltk.tokenize import word_tokenize
post_words = word_tokenize(post_text) # turns the text into list of words
print(post_words)


# -------------------------
# Filtering stop words
# ------------------------- 
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
print(stop_words)

post_filtered = []
for word in post_words:  
    if word.lower() not in stop_words:
        post_filtered.append(word) # checking if given word is in this set
print(post_filtered)


# -------------------------
# Stemming
# -------------------------
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

post_stemmed = []
for word in post_filtered:
    post_stemmed.append(stemmer.stem(word))
print(post_stemmed)

for word in post_filtered:
    root = stemmer.stem(word) # looking closer at stemmed words
    if (root!=word):
        print(word,' --> ',root)


# ------------------------------
# Tagging parts of speech (POS)
# ------------------------------
post_pos = nltk.pos_tag(word_tokenize(post_text))
print(post_pos)
# ^ labelling words in sentence according to their POS eg 'noun'


# -------------------------
# Lemmatising
# -------------------------
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def translate_pos(tag):
    '''Convert NN/VB/JJ/RB to n/v/a/r (translating in
       order to apply lemmatiser to POS tags).'''
    if tag.startswith('J'):
        result = 'a'
    elif tag.startswith('V'):
        result = 'v'
    elif tag.startswith('R'):
        result = 'r'
    else:
        result = 'n'
    return(result)


for sentence in post_sent:
    post_pos = nltk.pos_tag(word_tokenize(sentence))
    for word,pos in post_pos:
        print(lemmatizer.lemmatize(word,translate_pos(pos)),end=' ')
        
print('\n') 

# -------------------------
#  Named entity recognition
# -------------------------
post_pos = nltk.pos_tag(word_tokenize(post_text))
tree = nltk.ne_chunk(post_pos)
print(tree)
# ^identifying phrases (small sequence of tokens) with some meaning




grammar = "NP: {<DT>?<JJ>*<NN>}"

chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(post_pos)
tree.draw()

print('\n') 


# -------------------------
# Sentiment analysis
# -------------------------
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

score = sia.polarity_scores(post_sent)
print(score)


