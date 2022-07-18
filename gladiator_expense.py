lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

gladiatro_expenses = 0
shield_counter = 0
for lost in range (1, lost_fight_count+1 ):

    if lost % 2 == 0:
        gladiatro_expenses += helmet_price

    if lost % 3 == 0:
       gladiatro_expenses += sword_price

       if lost % 2 == 0:
            gladiatro_expenses += shield_price
            shield_counter += 1

            if shield_counter == 2:
                   gladiatro_expenses += armor_price
                   shield_counter = 0

print(f"Gladiator expenses: {gladiatro_expenses:.2f} aureus")