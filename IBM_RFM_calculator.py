import datetime as dt
this_year = dt.datetime.now()

#==============================================
#improvement #1: need to add ic verification 
#reference; https://github.com/wmthor/mykad
#Use Pandas to identify the state in IC from this wiki: https://en.wikipedia.org/wiki/Malaysian_identity_card

#improvement #2: calculate the actual age with birth date instead of year only
ic = input(f"Please enter your mykad id (with -): ")
age = this_year.year - int(ic.split('-', 0))
if age > 18:
    x = "adult"
    print(f"Patient is adult, {age} years old.")
else:
    x = "not adult"
    print(f"Patient is underage, {age} years old.")

#==============================================
#functions: add weight
weight = float(input("Please enter patient's weight : "))
unit = input("Weight in (k)g or (l)bs? ")
if unit == 'k' or 'K':
    weight = weight/2.205 #convert to kilograms
elif unit == 'l' or 'L':
    weight = weight*2.205 #convert to pound
else:
    print("invalid weight, please enter again.")
print(f"Patient's weight is {kg}kg and {lbs}lbs")

#==============================================
#functions: add height

#==============================================
#functions: add wiast circumference

#==============================================
gender = input("Are you (m)ale or (f)emale? ")
if gender == 'm' or 'M':
    RFM = 64 - (20 * height / WC)

elif gender == 'f' or 'F':
    RFM = 76 - (20 * height /WC)

else:
    print("gender not identified.")


    



