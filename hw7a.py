def wordsGTn(n,str):
    w_len = []
    text = str.split(" ")
    for word in text:
        if len(word) > n:
            w_len.append(word)
    return w_len

inp = (str(input('Enter a Sentence (Only Strings Accepted): ')))

print ('\n\r')

print(wordsGTn(3, inp))
