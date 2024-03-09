import random
print("Password Generator")
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?'
number=int(input("How much do u want"))
length=int(input("length of the password"))
print('here are your passwords:')
for i in range(number):
    passwords=''
    for j in range(length):
        passwords+=random.choice(chars)
    print(passwords)


