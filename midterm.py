# Write a program which repeatedly reads strings until the user enters "0" (the digit zero). Once "0" is
# entered, print out the alphabetically highest string while converting all strings to lower case. For
# example, if the user enters the string s=’DUMBO’, internally the program will convert it with s.lower()
# to ‘dumbo’.
# Submit a Python script containing the program.
# Example transcript:
# Enter a string: apple
# Enter a string: DUMBO
# Enter a string: Colorado
# Enter a string: 0
# The highest string is: dumbo
# Note: Recall that Python string comparison ranks upper-case letters lower than lower-case letters,
# which is counter-intuitive. If the program had not converted ‘DUMBO’ and ‘Colorado’ to lower case,
# then it would print that ‘apple’ is the highest string.

# MID TERM

def userinput():

    loui = "" #empty string (means default value)
    user_list = [] #empty list

    while True:
        try:
            usin = str(input('Enter a string: ')).lower()  #intakes the users input and makes it automatically lowercase
        except ValueError:
            print('Please only enter a string!')

        if usin == '0':
            break

        elif usin > loui: #if the input has aleast one string then it will add to the empty list
            loui = usin

        else:
            pass

        user_list.append(usin) #adds the users input to the list
        print('List of Inputs: ', user_list) #shows the user the list is updating after every input

    print('\n\r')

    print('List of Inputs: ', user_list)

    print('The highest string is: ' + loui)

userinput()
