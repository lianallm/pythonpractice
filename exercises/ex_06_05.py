#PARSING
str = 'X-DSPAM-Confidence: 0.8475'

#find location of colon
ipos = str.find(':')
print(ipos)

#taking a part of the string and not including the first position of ipos
piece = str[ipos+2:]
print(piece)

#print (piece + 42.0) -> will fail/traceback

#converting the string to float
value = float(piece)
print(value)

print(value + 42.0)
