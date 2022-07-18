sum = input().split(' ')
number = int(input())
big = []
name_first = sum.pop(0)
name_last = sum.pop(-1)
list_left = []
list_rigtt = []
list_left = sum[:len(sum)//2]
list_rigtt = sum[len(sum)//2:]
#if len(list_rigtt) > 0 and len(list_left) > 0:
for y in range(number):
    if len(list_rigtt) > 0 and len(list_left) > 0:
     big.append(list_rigtt.pop(0))
     big.append(list_left.pop(0))
     if len(list_left) > 0 or len(list_rigtt) > 0:
          continue
for i in range(number):
              list_left = big[:len(big) // 2]
              list_rigtt = big[len(big) // 2:]
              big.append(list_rigtt.pop(0))
              big.append(list_left.pop(0))
#print(big)