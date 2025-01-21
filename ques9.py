import random
#9.1
def generate_random_numbers():
    random_numbers = random.sample(range(1, 101), 5)
    print("Random numbers:", random_numbers)

generate_random_numbers()

import random
#9.2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#9.3
def check_random_prime():
    random_number = random.randint(1, 100)
    print(f"Random number: {random_number}")
    if is_prime(random_number):
        print(f"{random_number} is a prime number.")
    else:
        print(f"{random_number} is not a prime number.")

check_random_prime()

import random
#9.4
def roll_die():
    result = random.randint(1, 6)
    print(f"You rolled a {result}.")

roll_die()

import random

def shuffle_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(numbers)
    print("Shuffled list:", numbers)

shuffle_list()

import random
#9.5
def select_random_item():
    items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    selected_item = random.choice(items)
    print("Randomly selected item:", selected_item)

select_random_item()

import random
#9.6
def pick_random_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    selected_card = random.choice(deck)
    print("Random card drawn:", selected_card)

pick_random_card()