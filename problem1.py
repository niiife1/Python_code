from math import  ceil
budged = float(input())
students = int(input())
price_for_flour = float(input())
price_for_one_egg = float(input())
price_for_one_apron = float(input())
free_flour = 0
total_budged = 0
rounded = ceil(students * 1.20)

if students >= 5:
    free_flour = students // 5
    total_budged = price_for_one_apron * (rounded) + (students * (price_for_one_egg * 10)) + ( price_for_flour * (students-free_flour))

else:
    total_budged = price_for_one_apron * (rounded) +(students * (price_for_one_egg * 10)) +(price_for_flour * students)


if budged >= total_budged:
    print(f"Items purchased for {total_budged:.2f}$.")


else:
    if budged < total_budged:
     budged -= abs(total_budged)
     print(f"{abs(budged):.2f}$ more needed.")