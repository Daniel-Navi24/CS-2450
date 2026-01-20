import random

print("Hello! I'm going to try to guess your age.")
name = input("What's your name? ")

guess = random.randint(15, 30)
print(f"Is your age {guess}? (y/n)")
answer = input().lower()

if answer == 'y':
    print(f"Yay! {name} is {guess} years old.")
else:
    print("Rats. Let me try again...")
