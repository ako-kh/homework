from random import randrange

n = randrange(1, 100)
life = 5

while life > 0:
    guess = int(input("guess the number (1-100): "))
    if guess == n:
        print("WIN")
        break
    else:
        life -= 1

        if guess < n:
            print("your number is lower")
        elif guess > n:
            print("your number is greater")
else:
    print("loss")