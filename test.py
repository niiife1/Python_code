data = list(map(int, input().split(" ")))

while True:
    command = input().split(" ")
    action = command[0]
    if action == 'End':
        break
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if index < 0 or index >= len(data):
            continue
        data[index] -= value
        if data[index] <= 0:
            data.remove(data[index])

    elif action == "Add":
        if 0 > index or index >= len(data):
            print("Invalid placement!")
        else:
            data.insert(index, value)

    elif action == "Strike":
        if index - value < 0 or index + value > len(data):
            print("Strike missed!")
            continue
        else:
            data = data[0:index - value] + data[index + value + 1:]

print('|'.join(map(str, data)))