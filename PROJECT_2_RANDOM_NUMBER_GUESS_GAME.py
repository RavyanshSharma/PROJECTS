# PROJECT 2 
import random

class NumberGuesser:
    def __init__(self):
        self.target = random.randint(1, 10)
        self.guesses = 0
    
    def check_guess(self, your_num):
        self.guesses += 1
        if your_num < self.target:
            return "Too low! Try a higher number."
        elif your_num > self.target:
            return "Too high! Try a lower number."
        else:
            return f"Congratulations! You guessed it in {self.guesses} tries."
    
    def __str__(self):
        return f"NumberGuesser: Target number between 1-10 (Guesses made: {self.guesses})"

# Continuous guessing game
game = NumberGuesser()
# Shows initial state
print(game)  

while True:
    guess = int(input("Enter your guess (1-10): "))
    result = game.check_guess(guess)
    print(result)
    if guess == game.target:
        break
 # Shows final state
print(game)  