numbers = list(map(int, input().split(",")))
numbers1 = []
group = 0
while True:
    numbers1.clear()
    group += 10
    if len(numbers)<= 0:
        break
    for x in numbers[:]:
     if x <= group:
        numbers.remove(x)
        numbers1.append(x)
    if len(numbers1) >= 0:
        print(f"Group of {group}'s: {numbers1}")