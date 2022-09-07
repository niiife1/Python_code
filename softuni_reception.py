from math import  ceil
employer_efficiency1 = int(input())
employer_efficiency2 = int(input())
employer_efficiency3 = int(input())
students_count = int(input())
all = students_count / (employer_efficiency1 + employer_efficiency2 + employer_efficiency3)
for i in range(1,int(all)):all+=1 if i % 3 == 0 else 0
print(f"Time needed: {ceil(all)}h.")
