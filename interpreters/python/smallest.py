i,s,d,p=input(),[(0,0)],[0]*30,0
while(s[-1])<len(i):
    if i[s[-1][1]]:
    if(c:=i[s[-1]])=="+":d[p]+=1
    if c=="-":d[p]-=1
    if c==">":p+=1
    if c=="<":p-=1
    if c==".":print(chr(d[p]),end="")
    if c==",":d[p]=ord(input())
    if c=="["and d[p]:
        s.append(s[-1])
    if c=="]":s.pop();continue
    print(s)
    s[-1]+=1
