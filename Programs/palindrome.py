nmb = int(input(“Give a number to check if palindrome:\n”))

tmp = nmb

revsd = 0

while (nmb > 0):

digit = nmb% 10

rev = rev * 10 + digit

nmb= nmb// 10

if (tmp == revsd):

print(“The number is palindrome!”)

else:

print(“Not a palindrome!”)
