def smi2sub(smi):
    with open(smi, 'r', encoding='ansi') as file:
        content = file.read()

    test=content.split('<SYNC Start=')
    #print(test)
    del test[0]
    sub=[]
    for i in range(len(test)):
        a=test[i]
        a=a.replace('><P Class=KRCC>', ' ')
        a=a.replace('&nbsp;', '')
        a=a.replace('\n', '')
        a=a.replace('<br>', '\n')
        a=a.replace('</BODY>', '')
        a=a.replace('</SAMI>','')
        blank=a.find(' ')
        A=a[:blank].strip()
        As=A[:-3]
        Am=A[-3:]
        A=As+'.'+Am
        B=a[blank:].strip()
        sub.append([float(A),str(B)])
    
    return sub
    
if __name__=="__main__":
    print(smi2sub("C:\esper\subtitles\Godzilla.Mothra.And.King.Ghidorah.Giant.Monsters.All-Out.Attack.2001.JAPANESE.1080p.BluRay.H264.AAC-VXT.smi"))