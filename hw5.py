#Use find and string slicing to extract the portion of the string after the
#colon character and then use the float function to convert the extracted
#string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'

ff = str.find(':') #find float
eos = len(str)  #end of string

n = (str[ff+1:eos]) #starts 1 space after : to the eos 

fn = float(n) #converts to float

print(fn)



