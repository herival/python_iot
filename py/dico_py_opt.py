import matplotlib.pyplot as plt
from string import punctuation
import sys

#We are not interested in words with less than MINLEN chars
MINLEN = 5

#load file in string
try:
    filename = 'testinput.txt'
    with open(filename, 'r', encoding='utf-8') as fi:
        data = fi.read()
        print(len(data), ' chars')
except Exception as e:
    print("Cannot read file "+filename)
    print("Reason: ",e)
    sys.exit(1)

# replace punctuation marks with spaces
# there are standard punctuation marks found in string.punctuation
# we need some additional marks found in the French text
# to avoid duplicates we merge the strings and convert them to a set
myPunctuation = set(punctuation+",.;!?()[]{}\'/`\""+"\u2019\u2018")
for c in myPunctuation :
   data = data.replace(c," ")

#everything lowercase
data = data.lower()

#separate words
words = data.split();
print(len(words), ' words')

#build wc - wordcount - as a dictionary giving the count of each word
wc = {w:words.count(w) for w in words if len(w)>MINLEN};
print(len(wc), ' unique words') 

#sort wordcount and show 10 most frequent
wc10 = sorted(wc, key=wc.get)[-10:][::-1] #this is a list
for w in wc10 :
    print(w, wc[w], sep="\t")

#output csv file with ";" as field separator (a French habbit)
try:
    filename = 'testoutput.csv'
    with open(filename, 'w') as fo:
        for w in sorted(wc):
            fo.write(w+";"+str(wc[w])+"\n") 
except Exception as e:
    print("Cannot write file "+filename)
    print("Reason: ",e)
    sys.exit(1)

    
#matplotlib output for 10 most frequent words
print(wc10)
wcl =  [wc[w] for w in wc10]
plt.bar(range(len(wc10)), wcl, align='center')
plt.xticks(range(len(wc10)), wc10)
plt.show()


# Success
sys.exit(0)
