print('If you had Overtime please type OTPay\nIf you had no Overtime please type Pay')   #number of hours
print('\n\r')
while True:
    tp = input("Please Enter OTPay or Pay\nType done to exit")
    try:
        if str(tp) == 'Pay':
            print('\n\r')
            print('Must have less than 40 Hours')
            Hours = input('Enter Hours:')
            float(Hours)
            Rate = input('Enter Rate:')
            float(Rate)
            print('\n\r')

            def computepay(Hours, Rate):
                Pay = (float(Hours) * float(Rate))
                return Pay

            def PrintMyResults(Hours, Rate, Pay):
                results = print ('Hours Entered:', Hours,'\n\r' 'Rate Entered:', Rate,'\n\r' 'Your Pay:', Pay)
                return PrintMyResults

            c = computepay(Hours,Rate)
            fp = PrintMyResults(Hours,Rate,c)
            x = float(Hours)    #converts Hours to an float
            y = 40      #base hours

            if x > y:             #if hours is > 40 hours: overtime
                print('Go to OTPay')      #("Pay:", round(float(OT),2))
            elif x < y:            #if hours is < 40 hours: regular pay
                print('\n\r')
                print("Pay:", round(float(fp),2))
            elif x == y:            #if hours is = 40 hours: regular pay
                print('\n\r')
                print("Pay:", round(float(fp),2))
            else:
                pass

        if str(tp) == 'OTPay':
            print('\n\r')
            print('Must have over 40 Hours')
            Hours = input('Enter Hours:')
            float(Hours)
            Rate = input('Enter Rate:')
            float(Rate)
            print('\n\r')

            def computepay(Hours, Rate):
                OT = (float(Hours) - 40) * (float(Rate) * float(1.5)) + (float(40) * float(Rate)) #overtime rate
                return OT
            def PrintMyResults(Hours, Rate, Pay):
                results = print ('Hours Entered:', Hours,'\n\r', 'Rate Entered:', Rate,'\n\r', 'Your Pay:', Pay)
            c = computepay(Hours, Rate)
            fp = PrintMyResults(Hours,Rate,c)
            x = float(Hours)    #converts Hours to an float
            y = 40      #base hours

            if x > y:             #if hours is > 40 hours: overtime
                print('\n\r')
                print("Pay:", round(float(fp),2))
            #elif x < y:            #if hours is < 40 hours: regular pay
                #print("Pay:", round(float(Pay),2))
            #elif x == y:            #if hours is = 40 hours: regular pay
                #print("Pay:", round(float(Pay),2))
            else:
                pass
        if str(tp) == 'done':
            print('\n\r')
            print('You have now exited the program!')

    except:
        print('Please Review Your Input & Prompt!')
