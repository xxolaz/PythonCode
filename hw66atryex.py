def makecaps():
    lineDefault = 0
    for line in file:
        lineDefault = lineDefault + 1
    print('Line', lineDefault)

    count = 0
    for line in file:
        count += 1
        print('Line{}: {}'.format(count, line.upper().strip()))

first_file = print('hw6char.txt')
second_file = print('hw6revisedchar.txt')

print('Available Files: hw6char.txt, hw6revisedchar.txt')

file_name = input('Please enter the name of the file you would like to use:')

try:
    file_name == (first_file)
    second_file == (second_file)
    results = open(file_name)
    file = results.readlines()

    makecaps()

except:
    print('File not found. Please check spelling and try again.')
    exit()
