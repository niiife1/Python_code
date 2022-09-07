from random import randrange

n = input().split(' ')
l = [randrange(n-i) for i in range(n)]


for i in l:   # the randomized, partial indices
    j = 0                         # aux variable
    while j <= i:                 # we will increment j later
        if j in indices:          # if this number j, smaller than i, is in the
             i += 1               # list of used indices, i must be incremented
        j += 1
    indices.append(i)