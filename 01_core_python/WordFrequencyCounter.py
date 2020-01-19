"""
A Program that downloads a web page requested by the user and reports up to ten most frequently used words. 
The program treats all words as case-insensitive, assuming that a word is described by the regular expression r"\w+".
"""
import re
from collections import Counter
import urllib.request 

try:
    with urllib.request.urlopen("https://www.cnn.com") as doc: 
        html = doc.read().decode('utf-8')
except:
    print("Could not open %s" % doc)
    raise

words = re.split(r"\W+", html, flags=re.IGNORECASE)
cntr = Counter(words)
print(cntr.most_common()[:10])
