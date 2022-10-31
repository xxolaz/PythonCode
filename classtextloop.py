fhandle = open('myFileName.txt')
lineCount = 0

for line in fhandle:
    lineCount = lineCount + 1
print('Line Count', lineCount)
