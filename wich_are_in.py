substring = input().split(', ')
sentence = input()
result = [el for el in substring if el in sentence]
print(result)