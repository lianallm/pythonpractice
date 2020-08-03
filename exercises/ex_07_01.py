#READING AND MANIPULATING TEXT FILES

fh = open('mbox-short.txt')
print(fh)

for lx in fh:
    #strips the blank lines from the right
    ly = lx.rstrip()
    #makes it uppercase
    print(ly.upper())
