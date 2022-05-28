import random


n = random.randint(1,99)

guess = int(input("Shkruaj nje numer prej 1 deri 99: "))


tentimet = 0

while n != guess:
    tentimet+=1
    if guess < n:
        print("Numri juaj eshte me i vogel se numri randon kjo eshte hera e", tentimet,"qe keni provuar")
        guess = int(input("Enter a number between 1 and 99 again: "))
    elif guess > n:
        print("Numri juaj eshte me i madh se numri randon kjo eshte hera e", tentimet,"qe keni provuar")
        guess = int(input("Enter a number between 1 and 99 again: "))

if guess == n:
    print("SAKT!! E gjetet ne", tentimet + 1,"tentime")

