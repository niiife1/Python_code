def get_line(i, n):
    space_count = n - 1 - i
    stars_count = i + 1
    return ' ' * space_count + ('* ' * stars_count).strip()

def print_line(n):
        print(get_line(n - 1, n - 1))

def print_squeare(n):
    [print(get_line(n -1, -1 )) for _ in range(n) ]



def print_rhombus(n):
    [print(get_line(i,n)) for i in range(n)]
    [print(get_line(i,n)) for i in range(n - 2, -1, -1)]


print_rhombus(3)
print_rhombus(4)
print_line(4)
print_squeare(5)