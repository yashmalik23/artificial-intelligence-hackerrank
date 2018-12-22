x,y=list(map(int,input().split()))
l,n=list(map(int,input().split()))
m=[]
a=[]
for i in range(l):
    f=list(input())
    m.append(f)
for i in range(l):
    for j in range(n):
        if m[i][j]=='d':
            a.append([i,j])
if(m[x][y]=='d'):
    print('CLEAN')
else:
    b=[abs(x-a[i][0])+abs(y-a[i][1]) for i in range(len(a))]
    pi,pj=a[b.index(min(b))][0],a[b.index(min(b))][1]
    vs=x-pi
    hs=y-pj
    if(vs<0):
        print('DOWN')
    elif(vs>0):
        print('UP')
    elif(hs<0):
        print('RIGHT')
    elif(hs>0):
        print('LEFT')
