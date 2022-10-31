#Homework 1

#Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.

Hours = input('Enter Hours:')    #number of hours

Rate = input('Enter Rate:')   #hourly rate

OT = (float(Hours) - 40) * (float(Rate) * float(1.5)) + (float(40) * float(Rate)) #overtime rate

Pay = float(Hours) * float(Rate) #Regular pay caluclation

x = float(Hours)    #converts Hours to an float
y = 40      #base hours


if x > y:             #if hours is > 40 hours: overtime
    print("Pay:", round(float(OT),2))
elif x < y:            #if hours is < 40 hours: regular pay
    print("Pay:", round(float(Pay),2))
elif x == y:            #if hours is = 40 hours: regular pay
    print("Pay:", round(float(Pay),2))
else:                   #if user doesnt input a float/int then returns an error
    print('Please enter a number!')
