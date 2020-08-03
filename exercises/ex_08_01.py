#FINDING CERTAIN INFO IN DATA/ SPLITTING STUFF IDK
han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    #there's an empty list so it tracebacks, or it has 2 items which also tracebacks
    # if len(wds) < 3 :
    #     continue
    # if wds[0] != 'From' :
    #     continue

    #shorter version of above code/ make sure the first if is in order!
    if len(wds) < 3 or wds [0] != 'From' :
        continue
    print(wds[2])
