from collections import  deque


cups = deque([int(x) for x in input().split(" ")])
bottle = [int(u) for u in input().split(" ")]

wasted = 0
wasted_water = 0

while cups and bottle:
    cup = cups.popleft()
    bottl = bottle.pop()

    if cup > bottl:
        wasted_water = cup - bottl
        cups.appendleft(wasted_water)
    else:
        wasted += bottl - cup

else:
        if len(cups) > 0:
            print(f"Cups: {(' '.join(map(str,cups)))}")
            print(f"Wasted litters of water: {wasted}")
        else:
            print(f"Bottles: {(' '.join(map(str,bottle)))}")
            print(f"Wasted litters of water: {wasted}")