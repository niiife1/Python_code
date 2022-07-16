list_elements = input().split( )
list_elements = list(map(int, list_elements))
# def decrease(number):
#     return  number -1
while True:
    elements = input().split( )
    command = elements[0]
    symbol = None
    symbol1 = None
    if command == 'end':
        break
    if command == 'decrease':
        #list_elements = map(lambda x: x -1 ,list_elements)
        list_elements1 = [x-1 for x in range(list_elements)]
        continue
    if command == 'swap':
        symbol = int(elements[1])
        symbol1 = int(elements[2])
        list_elements[symbol], list_elements[symbol1] = list_elements[symbol1], list_elements[symbol]
        continue
    if command == 'multiply':
        symbol = int(elements[1])
        symbol1 = int(elements[2])
        multiply = list_elements[symbol] * list_elements[symbol1]
        list_elements.pop(symbol)
        list_elements.insert(symbol,multiply)
        continue
print(', '.join(map(str, list_elements)))