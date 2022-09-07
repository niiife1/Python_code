number = int(input())
total_liters = 0
for num in range(number):
       liters = int(input())

       if liters + total_liters <= 255:
        total_liters += liters
        continue
       print("Insufficient capacity!")
print(total_liters)

