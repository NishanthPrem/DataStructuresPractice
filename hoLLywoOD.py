s=input()
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="abcdefghijklmnopqrstuvwxyz"
x=set(a)
y=set(b)
q=[]
sum=""
p=""
h=list(s)
v=[]
for i in s:
    if i in x:
        sum+=i
for j in  s:
    if j in y:
        sum+=j
print(sum)
rsum=sorted(sum)
print(rsum)
for i in rsum:
    p+=i

for i in p.upper():
    q.append(i)
q.sort()
print(q)
for i in p.lower():
    v.append(i)
v.sort()
print(v)
for i in range(len(s)):
    for j in h:
        if q[i] in h:
            print(q[i],end="")
            h.remove(q[i])
        elif q[i].lower() in h:
            print(q[i].lower(),end='')
            h.remove(q[i].lower())

        
        