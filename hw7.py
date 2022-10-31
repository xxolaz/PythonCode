def chop(L):
    if L: # "if L" checks if the list is not empty
        L.pop(0)
        if L: # L may be empty now
            L.pop(len(L)-1)

def middle(L):
    nm = L[1:] #contains all but the first element
    del nm[-1]
    return nm

print('Check Expect 1 chop')

# Tests for Chop
L = [4, 5, 6]
print(L)
print(chop(L))
print(L)

print('Check Expect 2 chop')

L = [34, 8, 9, 10, -4, 6, 9]
print(L)
print(chop(L))
print(L)

print('Check Expect 3 chop')

L = []
print(L)
print(chop(L))
print(L)

print('Check Expect 4 chop')

L = ['onlyone']
print(L)
print(chop(L))
print(L)

print('Check Expect 1 middle')

# Tests for middle
L = [4,5,6]
print(L)
print(middle(L))
print(L)

print('Check Expect 2 middle')

L = [34, 8, 9, 10, -4, 6, 9]
print(L)
print(middle(L))
print(L)
