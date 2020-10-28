def strip_punctuation(word):
    for punc in punctuation_chars:
        if punc in word:
            word=word.replace(punc,"")
    return word

def get_pos(line):
    pos=0
    list_of_words=line.split()
    list2=[]
    for each in list_of_words:
        list2.append(strip_punctuation(each))
    for word in list2:
        if word in positive_words:
            pos+=1
    return pos

def get_neg(line):
    neg=0
    list_of_words=line.split()
    list2=[]
    for each in list_of_words:
        list2.append(strip_punctuation(each))
    for word in list2:
        if word in negative_words:
            neg+=1
    return neg

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
                if lin[0] != ';' and lin[0] != '\n':
                    negative_words.append(lin.strip())
            

wr=open("resulting_data.csv","w")
main=open("project_twitter_data.csv","r")
#print(main.read())
lines=main.readlines()
#header=lines[0]

wr.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
for line in lines[1:]:
    lstline=line.split(",")
    if "\n" in lstline[-1]:
        lstline[-1]=lstline[-1].replace("\n","")
    b=lstline[-1]
    a=lstline[-2]
    c=get_pos(lstline[0])
    d=get_neg(lstline[0])
    e=c-d
    r=[a,b,c,d,e]
    wr.write(str(r))
    wr.write("\n")
wr.close()
main.close()