def palindore(single_num):

    single_num = list(single_num)
    other_way = single_num.copy()
    other_way.reverse()
    if other_way == single_num:
        print('True')
    else:
        print('False')

numbers = input().split(', ')
for number in numbers:
    palindore(number)