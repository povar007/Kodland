import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b = int(input("Введите длину пароля"))
password = ""
for i in range(b):
    password += random.choice(a)
print(password)
