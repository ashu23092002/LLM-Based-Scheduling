import json
import pandas as pd

import cleantext

import spacy
# https://www.tutorialspoint.com/adding-space-between-potential-words-using-python
# Using spaCy for auto-spacing

"""
spacy function for adding spaces
Not enough words in dataset of model
Most of the words got appended
"""
# def add_spaces(text):
#    nlp = spacy.load('en_core_web_sm')
#    doc = nlp(text)
#    words = []
#    for token in doc:
#       if not token.is_space:
#          words.append(token.text)
#       else:
#          words.append(' ')
#    return ''.join(words)
 
with open('doc1.json', 'r', encoding = 'utf-8') as f:
    docString1 = json.load(f)

# print(docString1)
print(type(docString1))
print(docString1.keys())
# print(dir(docString1))
# print(help(docString1))
print(docString1.get('page_1'))
print(type(docString1.get('page_1')))

"""
spacy didn't work
"""
# file = open("combined_doc_processed.txt",'a',encoding='utf-8')

# for i in range(1,11):
#     docstring = 'doc' + str(i) + '.json'
#     with open(docstring, 'r', encoding = 'utf-8') as f:
#         docData = json.load(f)
#     for rawValue in docData.values():
#         value = add_spaces(rawValue)
#         file.write(value)

"""
Combining all data in json file into a single text file
"""
# file = open("combined_doc.txt",'w')
# file.close()

# file = open("combined_doc.txt",'a',encoding='utf-8')

# for i in range(1,11):
#     docstring = 'doc' + str(i) + '.json'
#     with open(docstring, 'r', encoding = 'utf-8') as f:
#         docData = json.load(f)
#     for value in docData.values():
#         file.write(value)

"""
cleantext Based text cleaning
"""
file = open("combined_doc_processed.txt",'w',encoding='utf-8')
file.close()

file = open("combined_doc_processed.txt",'a',encoding='utf-8')

for i in range(1,11):
    docstring = 'doc' + str(i) + '.json'
    with open(docstring, 'r', encoding = 'utf-8') as f:
        docData = json.load(f)
    for rawValue in docData.values():
        value = cleantext.clean(rawValue,lowercase=True,punct=True,extra_spaces=True,stopwords=True)
        file.write(value)

# file.close()