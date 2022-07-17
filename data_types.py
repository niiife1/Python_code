def first_devide(string1,intiger1):
    if string1 == 'int':
        return int(intiger1) * 2
    if string1 == 'real':
        return (f'{int(intiger1) * 1.5:.2f}')
    if string1 == 'string':
        return (f"${intiger1}$")

name = input()
num = input()
print(first_devide(name,num))