file = open('climate_tweets.csv','r')
filename = "myfileY.txt"
filename2= "myfileN.txt"
outfile = open(filename, "w")
outfile2=open(filename2,'w')
punctuations = '''!()-[]{};'":\/,<>.|?@#$%^&*_~1234567890'''
for line in file.readlines():
    
    words=line.split()
    
    if 'Y' in words[-1]:
        for word in words:
            word=word.lower()
            if 'http' in word:
                outfile.write(word + "\n")
            else:
                for x in word: 
                    if x in punctuations: 
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
                    if x in punctuations: 
                        word=word.replace(x,"") 
                outfile2.write(word + "\n")