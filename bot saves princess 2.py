n=int(input())
bi,bj=list(map(int,input().split()))
m=[]
for i in range(n):
    i=input()
    m.append(i)
for i in range(n):
    for j in range(n):
        if m[i][j]=='p':
            pi=i
            pj=j
vs=bi-pi
hs=bj-pj
if(vs<0):
    print('DOWN')
elif(vs>0):
    print('UP')
elif(hs<0):
    print('RIGHT')
elif(hs>0):
    print('LEFT')
