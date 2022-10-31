#Chapter 3 Excercise 3

# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:


Score = input('Enter Score:')

x = float(Score) #coverts Score to an int

if x >= 0.9:
    print('A')
    
elif x >= 0.8:
    print('B')

elif x >= 0.7:
    print('C')
    
elif x >= 0.6:
    print('D')

elif x < 0.6:
    print('F')
    
else:
    print('Bad Score')
