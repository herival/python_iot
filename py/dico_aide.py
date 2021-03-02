import string
replace_char = string.punctuation+"\u2018"+"\u2019"+"€"+"\n"+"—"

dic = dict()

with open("testinput.txt") as f:
    text_file = "".join(f.readlines())

for char in replace_char:
    text_file = text_file.replace(char," ")
text_file = text_file.lower()
print(text_file)
print()
#print(text_file.split())
for word in text_file.split(" "):
    if len(word)>5:
        if not word in dic:
            dic[word]=0
        dic[word] += 1
print(dic)
print(sorted(dic, key=dic.get, reverse=True))
