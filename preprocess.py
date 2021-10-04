#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:11:22 2021

@author: wanyongfeng
"""

import pandas as pd
import numpy as np
import re

true = pd.read_csv("True.csv")
# false = pd.read_csv("Fake.csv")

textst = list(true.loc[:,"text"])
# textsf = list(false.loc[:,"text"])

# texts = np.array(textst + textsf)
texts = np.array(textst)

words = set()
punc = '''!()-[]{};:'"\,<>./?@#%^&*_~”“’'''
for idx, text in enumerate(texts):
    for ele in text:
        if ele in punc:
            text = text.replace(ele, "")
    text = re.sub(' +', ' ', text)
    text = text.lower()
    texts[idx] = text    
    temp = text.split()
    words = words.union(set(temp))
print(texts[0])

words = list(words)
element = dict.fromkeys(words, 0)
elements = []

for idx, text in enumerate(texts):
    element = dict.fromkeys(words, 0)
    temp = text.split()
    for j in temp:
        element[j] = element[j] + 1
    elements.append(element)
print(elements[0])