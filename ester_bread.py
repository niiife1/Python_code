budged = float(input())
price_for_one_flour = float(input())
price_for_1packegg = price_for_one_flour * 0.75
price_1kg_milk = price_for_one_flour * 1.25
milk_for_one_bred = price_1kg_milk / 4
eggs_earn = 0
bread_counter = 0
bread = 0
bread = price_for_one_flour + price_for_1packegg + milk_for_one_bred
while True:
    if budged > bread:
        #bread = price_for_one_flour + price_for_1packegg + milk_for_one_bred
        budged -= bread
        bread_counter += 1
        eggs_earn += 3
    if bread_counter % 3 == 0:
        eggs_earn -= (bread_counter - 2)
    if budged > bread:
          break
print(f'You made {bread_counter} loaves of Easter bread! Now you have {eggs_earn} eggs and {budged:.2f}BGN left.')