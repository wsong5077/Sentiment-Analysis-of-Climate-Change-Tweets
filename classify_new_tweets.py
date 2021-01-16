file = open('climate_test.csv','r')
punctuations = '''!()-[]{};'":\/,<>.|?@#$%^&*_~1234567890'''
filec = open("wordcount.csv",'r')
filename="yesorno.txt"
outfile = open(filename, "w")
#word, Y_counts, N_counts, Total_count
#P(word|Y)=P(Y|word)P(word)/P(Y)
#P(word|N)=P(N|word)P(word)/P(N)
totalY=0
totalN=0
for line in filec.readlines()[1:]:
    line=line.replace('\n','')
    values=line.split(',')
    totalY+=int(values[1])
    totalN+=int(values[2])
total=totalY+totalN
py=totalY/total
pn=totalN/total
print(totalY,totalN)
yscores={}
nscores={}
print(py)
print(pn)
for line in filec.readlines()[1:]:
    line=line.replace('\n','')
    values=line.split(',')
    word=values[0]
    y=int(values[1])
    n=int(values[2])
    yscores[word]=y
    nscores[word]=n
def mul(lst):
    result=1
    for x in lst:
        result=result*x
    return result

for line in file.readlines()[1:]:
    yscore=1.0
    nscore=1.0
    if "," in line:
        line=line.replace(',',' ')
    words=line.split()
    tnum=words[0]
    lsty=[]
    lstn=[]
    for word in words[1:]:
        word=word.lower()
        if 'http' in word:
            pass
        else:
            for x in word: 
                if x in punctuations: 
                    word=word.replace(x,"")        
            if word in yscores.keys() or word in nscores.keys():
                yscoreeach=yscores[word]/totalY
                nscoreeach=nscores[word]/totalN
                lsty.append(yscoreeach)
                lstn.append(nscoreeach)
    #print(lsty)
    yscore=mul(lsty)
    nscore=mul(lstn)
    #print("{:.10f},{:.10f}".format(yscore,nscore))
    yscore=yscore*py
    nscore=nscore*pn
    
    if yscore>=nscore:
        outfile.write(tnum + " "+ "Y" +  "\n")
    else:
        outfile.write(tnum+  " "+'N'  + "\n")

