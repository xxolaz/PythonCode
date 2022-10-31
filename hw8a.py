
emails = dict()                   #Opens the dictionary
fn = input('Enter file name: ')


try:
    fh = open(fn)
except FileNotFoundError:
    print('File cannot be found/opened:', fn)
    exit()

for line in fh:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    else:
        if words[1] not in emails:
            emails[words[1]] = 1
        else:
            emails[words[1]] += 1

sm = sorted(emails.items(), key = lambda x: x[1], reverse = True) #puts the emails in a list from the dictionary, then sorts the list by value from least to greatest, then reverse = True makes it greatest to least. 

print(*sm, vertical = '\n') #prints the list in a more readable format


#print(emails)
