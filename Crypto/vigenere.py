e_String="cidb^}jwzLVz@DV\zQJzGW@DNX"
d_String=""
key="xxdvce"
for i in range(len(e_String)):
    d_Char = chr((ord(e_String[i])-ord(key[i]))%26+ord('a'))
    d_String = d_String + d_Char
print( d_String )
