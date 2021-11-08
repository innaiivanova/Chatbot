# Codecademy's review of text processing
# Inna I. Ivanova
# Text pulled from https://en.wikipedia.org/wiki/Oprah_Winfrey

import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

oprah_wiki_no_tag = re.sub(r'<.?p>', '', oprah_wiki)

oprah_wiki_no_period = re.sub(r'\.', '', oprah_wiki_no_tag)

oprah_wiki_lower = oprah_wiki_no_period.lower()

oprah_wiki_tokenized = word_tokenize(oprah_wiki_lower)

oprah_wiki_lemmatized = [lemmatizer.lemmatize(token) for token in oprah_wiki_tokenized]
 
print(oprah_wiki_lemmatized)
