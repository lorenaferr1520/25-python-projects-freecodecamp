import random
from rich import print
def titulo(): # ASCII title

    print('''[green]=================================================================
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
=================================================================[/]''')
def hangman(): # ASCII hangman
    if count == 0:
        print('''[blue]
  +---+
  |   |
      |
      |
      |
      |
=========[/blue]''')
    elif count == 1:
        print('''[yellow]
  +---+
  |   |
  O   |
      |
      |
      |
=========[/yellow]''')
    elif count == 2:
        print('''[yellow]
  +---+
  |   |
  O   |
  |   |
      |
      |
=========[/yellow]''')
    elif count == 3:
        print('''[yellow]
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========[/yellow]''')
    elif count == 4:
        print('''[#fb8500]
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========[/#fb8500]''')
    elif count == 5:
        print('''[#fb8500]
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========[/#fb8500]''')
    elif count == 6:
        print('''[red]
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========[/red]''')

def line(): # Print duble line
    print('=================================================================')

words = ['dog', 'cat', 'house', 'car', 'tree', 'book', 'fish', 
         'bird', 'moon', 'star', 'rain', 'fire', 'cake', 
         'milk', 'door', 'lamp', 'shoe', 'frog', 'wind', 'boat']

word = random.choice(words)
hidden_word = []

for i in range(len(word)):
    hidden_word.append("___  ")
    
count = 0
win = False

titulo()
print('The word is...')
line()
for i in hidden_word:
    print(i, end= '')


hangman()


