import random

letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbols=")(*&^%$#@!)"

length=int(input("enter password length"))

all=letter+number+symbols

password=""

for i in range(length):
 password+=random.choice(all)

print("password=>",password)
