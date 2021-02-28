import random

number = random.randint(1,10)
guess = 0
count = 0
name = input("Howdy, May I know your name? ")
print("Hello "+name+".")
question = input("Are you ready  to guess? ")
if question.lower() == 'n':
    print("Oh, alright. we'll meet again.")
elif question.lower() == 'y':
    while not (guess == number):
        print("I'm thinking of a number between 1 & 10")
        guess=int(input("What's your guess?"))
        count = count + 1
        if guess==number:
            print("Briliant")
            print( f"Congrats, you guessed correctly. The number was indeed {guess}") 
            print(  f"It had taken you {count} tries") 
        elif guess > number:
            print("Think lower")
        elif guess < number:
            print("Think Higher")
        
       
    

            
