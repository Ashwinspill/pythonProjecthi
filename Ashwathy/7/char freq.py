s=input("enter the string : ")
dic={}
for n in s:
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
for m,n in dic.items():
    print(m,n)

