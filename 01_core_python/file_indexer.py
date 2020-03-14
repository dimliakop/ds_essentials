""" Example:
    {..., 'aloha': ['early-internet.dat', 'hawaiian-travel.txt'], ...}
"""
import glob
import re
import pickle

filenames = glob.glob("/path/to/the/files/*")

d = {}
s = ""
for filename in filenames:
    try:
        with open(filename) as fin:
            s = fin.read()
    except:
        pass
    words = re.findall(r'\w+', s)
    for word in words:
        if word in d:
            d[word].append(filename)
        else:
            d[word] = [filename]

with open("myData.pickle", "wb") as fout:
    pickle.dump(d, fout)
