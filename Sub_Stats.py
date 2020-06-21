import collections
from stop_words import get_stop_words

with open('corpus.txt', 'r') as file:
    data = (file.readlines())

print('Number of all Headlines:', len(data))

words = []
chars = []

for head in data:
    temp = head.replace('â€“', ' ').split()
    words.extend(temp)
    temp = list(head.replace('â€“', ' '))
    chars.extend(temp)

print('Number of all Words:', len(words))

stop_words = get_stop_words('en')

stop_words_in_heads = [word for word in words if word in stop_words]
print('Number of all StopWords', len(stop_words_in_heads))

print('Number of all Characters:', len(chars))

print('Average of Words per Headline:', 283/48)

print('Average of Characters per Words:', 1944/283)

print('Average of Characters per Headlines', 1944/48)

print('Average of StopWords per Headline', len(stop_words_in_heads)/48)