#DICTIONARIES PRACTICE

#asks for file and opens it
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

#making dictionrary
di = dict()

#takes away extra lines
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    #goes through each key 'w' in dictionary of words
    for w in wds:
        #gets the number value of key 'w' or makes it zero if didn't exist
        # idiom : retrieve/ create/ update/ counter
        di[w] = di.get(w,0) + 1
        #print(w, 'new', di[w]

        #breakdown:
        # oldcount = di.get(w,0) + 1
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        #for each string in the dictionary, if the string is in the di, then add 1
        #if w in di :
        #    di[w] = di[w]+ 1
        #if not, then it is a new word and assign it 1.
        #else :
        #    di[w] = 1
        #print(w, di[w])

#print(di)

#how to find the most common word

#for each key and value in the dictionary 'di' (.items returns a view object and displays the key and value)
largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k #captures the word/key that had largest value

#prints the key with the largest value hehe
print(theword, largest)
