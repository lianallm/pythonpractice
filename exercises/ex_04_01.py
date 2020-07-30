#CREATING YOUR OWN FUNCTION

def computepay(hours,rate):
    if fh > 40 :
        reg = hours * rate
        otp = (fh - 40.0) * (fr * 0.5)
        pay = reg + otp
    else:
        pay = fh * fr
    print("Pay:", xp)
    return pay


#defining work hours and rate of pay per hour
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

#anticipating user to input errors to prevent traceback errors
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

#assigns function return value as a variable "xp"
xp = computepay(fh,fr)
