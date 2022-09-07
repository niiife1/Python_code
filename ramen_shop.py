from collections import deque

bowls_pack = [int(x) for x in input().split(", ")]
costumers = deque([int(x) for x in input().split(", ")])

while len(bowls_pack) and len(costumers) > 0:
    bowls = bowls_pack.pop()
    decre_costumers =  costumers.popleft()
    if bowls >= decre_costumers:
        remaining = bowls - decre_costumers
        if remaining == 0:
            continue
        bowls_pack.append(remaining)
    else:
        remaining = decre_costumers - bowls
        costumers.appendleft(remaining)

if len(costumers) <= 0:
    print("Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")


if len(bowls_pack) > 0:
    print(f'Bowls of ramen left: {(", ".join(map(str,bowls_pack )))}')
if len(costumers) > 0:
    print(f"Customers left: {(', '.join(map(str,costumers)))}")