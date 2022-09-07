
if_name = 0
rows = 6
cols = 6
first_hit = 0
second_hit = 0
name = input().split(",")
first  = name[0]
second = name[1]
matrix = []
for row in range(rows):
    row_elements = list(input().split())
    for col in range(cols):
       pass
    matrix.append(row_elements)
while True:
    comands = input().strip("()").split(", ")
    coma = [int(x) for x in comands]
    if_name += 1
    next_row = coma[0]
    next_col = coma[1]

    if matrix[next_row][next_col] == "W":
        matrix[next_row][next_col] = first_hit
        if if_name % 2==0:
            print(f"{name[1]} hits a wall and needs to rest.")
        else:
            print(f"{name[0]} hits a wall and needs to rest.")

    if matrix[next_row][next_col] == "T":
        if if_name % 2 == 0:
            print(f"{name[1]} is out of the game! The winner is {name[0]}." )
        else:
            print(f"{name[0]} is out of the game! The winner is {name[0]}.")
        break
    if matrix[next_row][next_col] == "E":
        if if_name % 2 == 0:
                print(f"{name[1]} found the Exit and wins the game!")
        else:
                print(f"{name[0]} found the Exit and wins the game!")
        break






