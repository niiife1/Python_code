gifts = input().split(' ')
gift_list = []
while True:
    store = input().split(' ')
    comand = store[0]
    materials = store[1]
    position = int(store[2]) if  len(store) > 2   else None

    if comand == 'OutOfStock':
        gifts = ['None' if x == materials else x for x in gifts]


    if comand == 'Required':
      if 'None' in gifts:
       gifts[position] = materials
          #if position == None:


       gifts[position] = materials

    if comand == 'JustInCase':
        gifts.pop()
        gifts.append(materials)
    if comand == 'No' and materials == 'Money':
        gifts = list(dict.fromkeys(gifts))
        gifts.remove('None')
        h = " ".join(gifts)

        break
print(h)