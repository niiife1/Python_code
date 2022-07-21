items = input().split(', ')
while True:
    command = input().split(' - ')
    first_comand = command[0]
    if first_comand == 'End':
        break
    item = command[1]
    if first_comand == 'Add':
        if item not in items:
            items.append(item)

    if first_comand == "Remove":
        if item  in items:
            items.remove(item)

    if first_comand == "Last":
        if item in items:
            items.remove(item)
            items.append(item)

    if first_comand == "Bonus phone":
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        if old_item in items:
            old_item = items.index(old_item)
            items.insert(old_item+1,new_item)

print(', '.join(items))


