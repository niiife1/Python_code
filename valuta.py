from forex_python.converter import  CurrencyRates

c = CurrencyRates()
amount = int(input('Напишете желаната сума: '))
from_currencyy = input('Напишете от коя валота ще променяте: ').upper()
to_currency = input('Напишете на коя валота изкате да пормените: ').upper()

print(amount, from_currencyy, '<---- НА ---->', to_currency)

result = c.convert(from_currencyy, to_currency, amount)
print(f'{result:.2f} {to_currency}')
