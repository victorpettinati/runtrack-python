L = [1, 2, 3, 4, 5]

l = len(L)
temp = L[0]
L[0] = L[l-1]
L[l-1] = temp

print (L)