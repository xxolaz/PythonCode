#Create a text file with Notepad or a text editor that does not add
#special characters and just stores plain text.  Add several lines of
#lowercase text inside this file (any data you'd like). Then write
#a Python program to read through this text file that you created
#and print the contents of the file (line by line) all in upper case.
#Submit your Python program and the input file and the output file.

#Using the Python program you created in hw6, create another text file.
#You now should have two text files.  Enhance the Python program to allow
#the user to enter the file name and include error checking to handle
#the situation where the user does not enter one of the two proper
#file names as input.  Submit the Python program and the output of
#your program.

def expro():

    lineCount = 0
    for line in file:
        lineCount = lineCount + 1
    print('Line Count', lineCount)

    print('\n\r')

    #adds number to lines from file
    count = 0
    for line in file:
        count += 1
        print('Line{}: {}'.format(count, line.upper().strip()))

print('Files: hw6textfile.txt,hw6textfile2.txt')
while True:
    #infile = (input('Please Enter the Name of File from the list! \n\r'))
    try:
        infile = (str(input('Please Enter the Name of File from the list! \n\r')))
    except ValueError:
        print('Check spelling of file & make sure it is one of the Files listed!')

    print('\n\r')

    try:
        if str(infile) == 'hw6textfile.txt':
            fhandle = open(infile)
            file = fhandle.readlines()
            expro()
            break

        elif str(infile) == 'hw6textfile2.txt':
            fhandle = open(infile)
            file = fhandle.readlines()
            expro()
            break

        else:
            print('Invaild Input!')

    except:
        print('Invaild File Name!')
