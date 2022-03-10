S = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
m = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
for key in range(len(S)):
t = ''
for s in m:
    if s in S:
        sI = S.find(s)
        tI = sI - key
        if tI < 0:
            tI = tI + len(S)
        t = t + S[tI]
    else:
        t = t + s
print('Key #%s: %s' % (key, t)) 
#Key #26: picoCTF{not_too_bad_of_a_problem}
