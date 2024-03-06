"""Guess a number between 1 and 10"""
import random

guess = int(input('Guess a number between 1 and 10: '))
count = 0
number = random.randrange(1, 11)
while guess != number:
    count += 1
    number = random.randrange(1, 11)
    if guess == number:
        print(f'Correct! You guessed the number {number} in {count} tries!')
    else:
        guess = int(input('Incorrect number! Guess again!: '))
