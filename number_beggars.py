line = input().split(' ')
beggers = int(input())
list_line = []
beggars_count = []
for i in (line):
    current_line = i.split(',')
    real_line = int(current_line[0])
    list_line.append(real_line)
for y in range (beggers):
  beggars_num = list_line[y::beggers]
  beggars_count.append(sum(beggars_num))
print(beggars_count)


