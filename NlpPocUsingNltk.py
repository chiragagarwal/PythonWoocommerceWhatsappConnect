import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize

sentence = "My name is Chirag Agarwal"
# sentence = "The United States of America's President stays in the White House"

sentence_tokens = word_tokenize(sentence)
print(sentence_tokens)
print(len(sentence_tokens))

sentence_tags = nltk.pos_tag(sentence_tokens)
print(sentence_tags)

sentence_chunks = ne_chunk(sentence_tags)
print(sentence_chunks)

# tokenization - break sentences into words/tokens
# stemming, lemmatization - stemming strips words from beginning and end, lemmatization actually finds the root word
# stop words - words which are used in english to complete sentences but are not useful for NLP
# parts of speech (noun, pronoun, verb etc)
# named entity recognition - 3 Phases:
# -- 1. Nouned phrase identification - done using tagging etc
# -- 2. Phrase classification - Classify the extracted nouns in step 1 to categories such as person, location etc - can be done by creating lookup tables, dictionaries etc 
# -- 3. Entity disambiguation - used to avoid misclassification of phrases/words into incorrect meaning. Can be implemented using creating a validation layer on top of the result using popular knowledge graphs such as google knowledge graph, IBM watson, wikipedia
# syntax tree - Syntax is governed by rules, principles and process. to understand it, you can create a syntax tree which is a tree representation of syntactic structure of sentences or strings. Use GhostScript.
# chunking - picking up INDIVIDUAL pieces of information and GROUPING then into bigger pieces.