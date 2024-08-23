def smi2sub(smi):
    with open(smi, 'r', encoding='ansi') as file:
        content = file.read()

    test=content.split('<SYNC Start=')
    del test[0]
    sub=[]
    for i in range(len(test)):
        a=test[i]
        a=a.replace('><P Class=KRCC>', ' ')
        a=a.replace('\n', '')
        a=a.replace('<br>', '\n')
        blank=a.find(' ')
        A=a[:blank].strip()
        As=A[:-3]
        Am=A[-3:]
        A=As+'.'+Am
        B=a[blank:].strip()
        
        if i%2:
            k=i//2
            sub[k].append(float(A))
        else:
            sub.append([float(A),str(B)])

    return sub
    
if __name__=="__main__":
    print(smi2sub('a.smi'))
    #print(smi2sub('test_timeNotyet.smi'))