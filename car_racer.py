def racer(all):
    count = 0
    for x in all:
        count += x
        if x == 0:
            count *= 0.8
    return count


res = input().split( )
left = list(map(int, res[:len(res)//2]))
right = list(map(int, res[len(res)//2:]))
right.pop(0)
all_left = racer(left)
all_right = racer(right)

if all_left > all_right:
    print(f'The winner is right with total time: {all_right:.1f}')
else:
    print(f'The winner is left with total time: {all_left:.1f}')

