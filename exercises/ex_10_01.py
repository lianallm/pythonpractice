#TUPLES PRACTICE 

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

#print(di)

#creating list of tuples
#x = sorted(di.items())
#prints up to, but not including 5
#print(x[:5])

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

#print(tmp) flipped

tmp = sorted(tmp,reverse=True) #reverse=True means reverse
#print(tmp[:5]) #sorted top 5

for v, k in tmp[:5]:
    print(k,v)
