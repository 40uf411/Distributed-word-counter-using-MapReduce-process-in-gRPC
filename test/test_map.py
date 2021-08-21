# meta data (input)
file = './inputs/pg-dorian_gray.txt'
M = 5
n= 1

# treatment
pos = lambda x: ord(x) - 97

text= ""
with open(file,"r") as file:
    text = file.read().lower()

# Tokenizing
text = ''.join([letter if letter in 'azertyuiopqsdfghjklmwxcvbn' else ' ' for letter in text])
tokens = text.split()

# Making tmp lists
tmp = list()
for i in range(M):
    tmp.append(list())

# Dispaching the words into their corresponding list
for token in tokens:
    p = pos(token[0]) % M
    tmp[p].append(token)

for idx, tmpFile in enumerate(tmp):
    with open('./tmp/mr-%i-%i'%(n, idx), 'w+') as file:
        file.write('\n'.join(tmpFile))