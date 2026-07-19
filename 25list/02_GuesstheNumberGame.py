import random
computer = random.randint(1, 10)
attempts = 0
user_number = int()

def line():
    print("=" * 30)

line()
print("GUESS THE NUMBER GAME".center(30))
line()

# user input
while True:
    while True:
        try:
            user_number = int(input('Choose a number from 1 to 10: '))
        except ValueError:
            print('Please, only numbers from 1 to 10.')
            continue
        if 1 <= user_number <= 10:
            break
        else:
            print('Please, only numbers from 1 to 10.')

    attempts += 1
    
    line()
    if user_number == computer:
        print('Congratulations! You won!')
        break

    elif user_number > computer:
        print("It's a smaller number, try again.")
        
    else:
        print("It's a higher number, please try again.")

# Game Over
print(f'Congratulations! The number was {computer}, you got it right after {attempts} tries.')
print('''
-----------------------------
╔═══╗         ╔═══╗
║╔═╗║         ║╔═╗║
║║ ╚╬══╦╗╔╦══╗║║ ║╠╗╔╦══╦═╗
║║╔═╣╔╗║╚╝║║═╣║║ ║║╚╝║║═╣╔╝
║╚╩═║╔╗║║║║║═╣║╚═╝╠╗╔╣║═╣║
╚═══╩╝╚╩╩╩╩══╝╚═══╝╚╝╚══╩╝
-----------------------------''')
    
        