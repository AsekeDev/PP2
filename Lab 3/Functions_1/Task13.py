import random
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
number_to_guess = random.randint(1, 20)
guesses = 0
while True:
    print("Take a guess.")
    number = int(input())
    guesses += 1
    if(number > number_to_guess):
        print("Your guess is too high.")
    elif(number < number_to_guess):
        print("Your guess is too low.")
    else:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        break
            
