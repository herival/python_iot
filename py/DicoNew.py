#Counter implementation for fast run
import string
from collections import Counter 

# File section
try:
    filename = 'testinput.txt'
    with open(filename, 'r', encoding='utf-8') as fi:
        data = fi.read()
        print(len(data), ' chars')
except Exception as e:
    print("Cannot read file "+filename)
    print("Reason: ",e)
    sys.exit(1)

#Punctuation replacement
replace_char = string.punctuation+"\u2018"+"\u2019"+"€"+"\n"+"—"+"…"
print("caractères remplacés :",replace_char)
trans_array=str.maketrans(replace_char," "*len(replace_char))

#Split in words
words = data.translate(trans_array).lower().split()
print(len(words),"words in file")

MINLEN = 5
result = Counter(w for w in words if len(w)>MINLEN).most_common(10)
#print(result)
for index, value in result :
    print(index, value)   
