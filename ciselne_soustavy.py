# ciselne_soustavy.py - prevod celych cisel do soustavy se zadanym zakladem
# Jan Nosek <nosekj@jirovcovka.net>

znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

file = open('vstup.dat','r', encoding="utf-8")
lines = file.readlines()
base  = int(lines[0].strip())
number = int(lines[1].strip())
originalNumber = int(lines[1].strip())
result = ''
sign = '' # prazdne kdyz kladne
if number < 0:
    number = abs(number)
    originalNumber = abs(originalNumber)
    sign = '-'


while number > 0:
    remainder = number % base
    result = znaky[remainder] + result
    number = number // base
result = sign + result
print(result)