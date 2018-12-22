n=int(input())
m=[]
for i in range(n):
    i=input()
    m.append(i)
for i in range(n):
    for j in range(n):
        if m[i][j]=='m':
            bi=i
            bj=j
        if m[i][j]=='p':
            pi=i
            pj=j
vs=bi-pi
hs=bj-pj
if(vs<=0):
    for i in range(abs(vs)):
        print('DOWN')
if(vs>0):
    for i in range(abs(vs)):
        print('UP')
if(hs<=0):
    for i in range(abs(hs)):
        print('RIGHT')
if(hs>0):
    for i in range(abs(hs)):
        print('LEFT')
