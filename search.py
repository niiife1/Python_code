number = int(input())
num = int(input())
all_num = list()


for i in range(number):
    all_num.append(int(input()))

print(all_num)
filtered = list()
for current_num in all_num:

    if num in current_num:
        filtered.append(current_num)
print(filtered)

