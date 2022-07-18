import re
barcode = input()
pattern = "(@#{1,})(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])(@#{1,})"
result = re.findall(pattern, info)

for res in result:
   if res  = res.isalnum():
