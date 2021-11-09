# Codecademy's natural language processing with regular expressions - review
# Inna I. Ivanova

from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from chunk_counter import chunk_counter

# define your own chunk grammar here
chunk_grammar = "Chunk: {<.*>+}"

# create RegexpParser object
chunk_parser = RegexpParser(chunk_grammar)

# create a list to hold chunked sentences
chunked_oz = list()

# create a for loop through each pos-tagged sentence in pos_tagged_oz
for pos_tagged_sentence in pos_tagged_oz:
  # chunk each sentence and append to chunked_oz
  chunked_oz.append(chunk_parser.parse(pos_tagged_sentence))

# store and print the most common chunks
most_common_chunks = chunk_counter(chunked_oz)
print(most_common_chunks)
