import glob
from collections import Counter
# input
r = 1
# treatment
files = glob.glob('./tmp/*-%i'%(r))
c = Counter([])

for file in files:
    txt = ''
    with open(file, 'r') as f:
        txt = f.read().split()
    c.update(txt)

with open('./out/out-%i'%(r), 'w+') as file:
        file.write('\n'.join('%s %s'%(word, count) for word, count in c.items()))