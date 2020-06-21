import numpy as np
import matplotlib.pyplot as plt

with open ('corpus.txt', 'r') as file:
    data = (file.readlines())

#print(data)

def making_dic(data):
    text = ' '.join(data).lower()
    chars = list(text)
    unique_chars = list(set(chars))
    return unique_chars

dic = making_dic(data)

zero_mat = np.zeros([len(dic), len(dic)])
def bi_count(head):
    for ind, char in enumerate(head):
        if (ind-1) > -1:
            char_index = dic.index(char)
            prev_index = dic.index(head[ind-1])
            zero_mat[char_index][prev_index] += 1
            zero_mat[prev_index][char_index] += 1
        
for head in data:
    bi_count(head.lower())

#print(zero_mat, dic, data)


plt.matshow(zero_mat)
plt.xticks(range(len(dic)), dic, fontsize=14, rotation=45)
plt.yticks(range(len(dic)), dic, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Characters Correlation Matrix', fontsize=16);
plt.show()  