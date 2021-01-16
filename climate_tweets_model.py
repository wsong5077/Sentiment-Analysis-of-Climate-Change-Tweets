file = open('climate_tweets.csv','r')
filename = "myfileY.txt"
filename2= "myfileN.txt"
outfile = open(filename, "w")
outfile2=open(filename2,'w')
punctuations = '''!()-[]{};'"\,<>.|?@#$%^&*_~1234567890'''
punctuationsrest=':/'
for line in file.readlines():
    for x in line:
        if x in punctuations: 
            line=line.replace(x," ") 
    
    words=line.split()
    
    if 'Y' in words[-1]:
        for word in words:
            word=word.lower()
            if 'http' in word:
                outfile.write(word + "\n")
            else:
                for x in word: 
                    if x in punctuationsrest: 
                        word=word.replace(x,"") 
                outfile.write(word + "\n")
    if 'N' in words[-1]:
        
        words=line.split()
        for word in words:
            word=word.lower()
            if 'http' in word:
                outfile2.write(word + "\n")
            else:
                for x in word: 
                    if x in punctuationsrest: 
                        word=word.replace(x,"") 
                outfile2.write(word + "\n")


existence={}
denial={}
file = open('myfileY.txt','r')
file2= open('myfileN.txt','r')
for aline in file.readlines():
    #print(existence)
    aline=aline.replace('\n','')
    if 'http' not in aline:
        if aline not in existence:
            existence[aline]=0
        existence[aline]=existence[aline]+1

for aline in file2.readlines():
    aline=aline.replace('\n','')
    if 'http' not in aline:
        if aline not in denial:
            denial[aline]=0
        denial[aline]=denial[aline]+1  

outfile = open("wordcount.csv", "w")
# output the header row
outfile.write('word, Y_counts, N_counts, Total_count')
outfile.write('\n')
# output each of the rows:
together={}
for akey in existence:
    together[akey]=existence[akey]
    if akey in denial:
        together[akey]=together[akey]+denial[akey]
    else:
        denial[akey]=0
        
        
for akey in denial:
    
    if akey in existence and akey not in together:
        together[akey]=existence[akey]+denial[akey]
    if akey not in existence and akey not in together:
        together[akey]=denial[akey]
        existence[akey]=0



for akey in together:
    
    row_string = '{},{},{},{}'.format(akey, existence[akey], denial[akey],together[akey])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()