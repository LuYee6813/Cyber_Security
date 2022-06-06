encrypt = "cidb^}jwzLVz@DV\zQJzGW@DNX"
decrypt = "FLAG{}jwzLVz@DV\zQJzGW@DN}"
el = [] 
dl = []
key_ord = []
key_chr = []

for e in encrypt:
    el.append(ord(e))

for d in decrypt:
    dl.append(ord(d)) 


for i in range(0,len(dl)):
    key_ord.append(el[i]-dl[i])
    
for j in range(0,len(key_ord)):
    print(key_ord[j])
