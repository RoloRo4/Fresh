import random

print ("Welcome to the Guessing Game! Here are the Rules: Guess a number between 1 and 100. The less guesses, the better!")

num = random.randint(1,100)
num_of_tries = 1

guess = int(input("Guess a number! "))

while guess < 1 or guess > 100:
    print ("OUT OF BOUNDS")
    guess = int(input("Guess a number! "))
    
if guess == num:
    print ("You guessed correctly on your first try!")
    
elif abs(guess - num) < 10:
    print ("WARM!")

elif abs(guess - num) > 10:
    print ("COLD!")


while guess != num:
    distance = abs(guess - num)
    newguess = int(input("Guess again! "))
    num_of_tries += 1
    
    if newguess == num:
        print (f"You guess correctly! It took you {num_of_tries} attempts to get it right.")
        break
    elif abs(newguess - num) < distance:
        print ("WARMER!")
        guess = newguess
    elif abs(newguess - num) > distance:
        print ("COLDER!")
        guess = newguess
    
    
    
    
