import collections
from matplotlib import pyplot as plt
from stop_words import get_stop_words

stop_words = get_stop_words('en')


def counter(words):
    c = collections.Counter(words)
    return c


with open('corpus.txt', 'r') as file:
    data = (file.readlines())


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
#frequency of words
data = [x.lower() for x in data]

words = []
for head in data:
    temp = head.replace('â€“', ' ').split()
    words.extend(temp)

cleaned_words = [x for x in words if x not in stop_words]


cleaned_words = dict(counter(cleaned_words).most_common(15))
ax1.barh(list(cleaned_words.keys()), cleaned_words.values())

#Frequency of chars
#print(list('ali'))
#for chars

chars = []
for head in data:
    temp = list(head.replace('â€“', ' '))
    chars.extend(temp)
#print(chars)

chars_count = dict(counter(chars).most_common(50))
ax2.barh(list(chars_count.keys()), chars_count.values())
plt.show()