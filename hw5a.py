print('Please Enter Data in the format, X-DSPAM-Confidence:0.4563')
str1 = ':'
while True:
    data = input('Enter Data in Specific to the Example:')
    try:
        data = str(data)
    except DataError:
        print('Invaild Input, Please Follow Example!')
    if str1 in data:
        print('Input Accepted!')
        break
    else:
        print('Invaild Input, Please Follow Example!')


ff = data.find(':') #find float
eos = len(data)  #end of string

d = (data[ff+1:eos])

fd = float(d)

print('\n\r')

print(fd)
