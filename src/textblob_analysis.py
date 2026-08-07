#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:52:12 2026

@author: miaemanuele
"""



import textblob
from textblob import TextBlob


# subjectivity = 0/objectivity/factual and 1/subjective/opinion
# polarity = -1/negative 0/neutral 1/positive



# -------------------------
# Creating TextBlob
# -------------------------  
post = TextBlob(''' Big link up tonight 🔥 
                8:30 @ Broadgate by the statue 
                bring fireworks 😂 don’t be soft 
                cov uni lot better show up 
                #CovTakeover #LinkUp #CityCentre ''')


# -----------------------------
# Part-of-Speech (POS) tagging
# -----------------------------
print(post.tags) # labelling words in sentence according to their POS eg 'noun'

print('\n') 


# -------------------------
# Sentiment analysis
# ------------------------- 
print(post.sentiment) # checking polarity and subjectivity
print(post.sentiment.polarity)

print('\n') 


# -------------------------
# Tokenisation
# ------------------------- 
print(post.words) # breaking TextBlob into words

print('\n') 


print(post.sentences) # breaking TextBlob into sentences

print('\n') 


for sentence in post.sentences:
    print(sentence.sentiment)

print('\n') 


# -------------------------
# Parsing
# ------------------------- 
print(post.parse())

print('\n') 


# -------------------------
# Lemmatisation
# ------------------------- 
from textblob import Word
w = Word('uni') # finding the lemma of this word
w.lemmatize()

w = Word('cov') # finding the lemma of this word
w.lemmatize()
