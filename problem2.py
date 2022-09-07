cars = input().split(">>")
total = 0

for command in cars:
    command = list(command.split(' '))
    car_name = command[0]
    years = int(command[1])
    kilometer = int(command[2])

    if car_name == "family":
        total_tax = 50 - (years * 5) + (kilometer // 3000)* 12
        total += total_tax
        print(f"A {car_name} car will pay {total_tax:.2f} euros in taxes.")
        continue

    if car_name == "heavyDuty":
        total_tax = 80 - (years * 8) + (kilometer // 9000) * 14
        total += total_tax
        print(f"A {car_name} car will pay {total_tax:.2f} euros in taxes.")
        continue

    if car_name == "sports":
        total_tax = 100 - (years * 9) + (kilometer // 2000) * 18
        total += total_tax
        print(f"A {car_name} car will pay {total_tax:.2f} euros in taxes.")
        continue

    else:
        print("Invalid car type.")

else:

    print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")