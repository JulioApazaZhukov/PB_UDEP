n = ['JC','EG','EY','MA','XY','AB']
a = ['MA','VC','ZH','IA','ZH','IA']

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j] or (a[i]==a[j] and n[i]>n[j]):
            a[i],a[j] = a[j],a[i]
            n[i],n[j] = n[j],n[i]

print(n)
print(a)