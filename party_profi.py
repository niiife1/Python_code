groub = int(input())
days = int(input())
coins = 0
#coins_all_days = coins -

for d in range (1,days +1):
 if d % 15 == 0:
    groub += 5

 if d % 10 == 0:
        groub -= 2

 if d % 1 == 0:
     coins += 50 - (groub * 2)

 if d % 3 == 0:
     coins -= (groub * 3)

 if d % 5 == 0:
  coins+= (groub * 20)

  if d % 3 == 0:
       coins -= (groub * 2)


print(f"{groub} companions received {int(coins / groub)} coins each.")