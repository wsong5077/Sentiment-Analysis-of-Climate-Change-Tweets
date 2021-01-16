openfile=open("climate_test_answers.csv","r")
openfile2=open("yesorno.txt","r")
dic={}
dic2={}
for line in openfile.readlines()[1:]:
    line=line.replace('\n','')
    line=line.split(',')
    iden=line[0]
    yon=line[1]
    dic[iden]=yon
for line in openfile2.readlines():
    line=line.replace('\n','')
    line=line.split(' ')
    iden=line[0]
    yon=line[1]
    dic2[iden]=yon
count=0
for key in dic:
    try:
        answer=dic[key]
        if answer in dic2[key]:
            count+=1
    except Exception:
        pass
print(count)

