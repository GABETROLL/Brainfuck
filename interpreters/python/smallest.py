c: str = input()
d = [0] * 30
p = 0
def b(i):
    global p
    while i<len(c):
        if c[i]=="+":
            d[p]+=1
        if c[i]=="-":
            d[p]-=1
        if c[i]==">":
            p+=1
        if c[i]=="<":
            p-=1
        if c[i]==".":
            print(chr(d[p]),end="")
        if c[i]==",":
            d[p]=ord(input())
        if c[i]=="[":
            ni=i
            while d[p]:
                ni = b(i + 1)
            i = ni
        elif c[i]=="]":
            return i
        i+=1
    return i
b(0)