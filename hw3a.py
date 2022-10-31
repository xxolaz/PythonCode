#Homework 3a

#Chapter 3 - Exercise 2:
#Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

print('If you had Overtime please type OTPay\nIf you had no Overtime please type Pay')   #number of hours
while True:
    tp = input("Please Enter OTPay or Pay")
    try:
        if str(tp) == 'Pay':
            print('Must have less than 40 Hours')
            Hours = input('Enter Hours:')
            float(Hours)
            Rate = input('Enter Rate')
            float(Rate)
            Pay = (float(Hours) * float(Rate))
            x = float(Hours)    #converts Hours to an float
            y = 40      #base hours
            if x > y:             #if hours is > 40 hours: overtime
                print("Pay:", round(float(OT),2))
            elif x < y:            #if hours is < 40 hours: regular pay
                print("Pay:", round(float(Pay),2))
            elif x == y:            #if hours is = 40 hours: regular pay
                print("Pay:", round(float(Pay),2))
            else:
                pass
        if str(tp) == 'OTPay':
            print('Must have over 40 Hours')
            Hours = input('Enter Hours:')
            float(Hours)
            Rate = input('Enter Rate')
            float(Rate)
            OT = (float(Hours) - 40) * (float(Rate) * float(1.5)) + (float(40) * float(Rate)) #overtime rate
            x = float(Hours)    #converts Hours to an float
            y = 40      #base hours
            if x > y:             #if hours is > 40 hours: overtime
                print("Pay:", round(float(OT),2))
            elif x < y:            #if hours is < 40 hours: regular pay
                print("Pay:", round(float(Pay),2))
            elif x == y:            #if hours is = 40 hours: regular pay
                print("Pay:", round(float(Pay),2))
            else:
                pass
    except:
        print('Please Enter a Number!')
