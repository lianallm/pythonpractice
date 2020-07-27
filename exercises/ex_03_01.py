#defining work hours and rate of pay per hour
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

#calculates overtime pay (over 40 hours)
if fh > 40 :
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,otp)
    xp = reg + otp
#calculates regular pay
else:
    print("Regular")
    xp = fh * fr

print("Pay:", xp)
