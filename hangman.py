import random

def menu():
    print("\n H  A  N  G  M  A  N")
    print()
    print(" 'N' - New Game")
    print(" 'Q' - Quit Game")
    print()
  
    while True:
        choice = input("Enter your choice >>> ").upper()
        
        if choice == 'N':
            print("\nChoose a Letter from the Alphabet. You have 6 tries.\n")
            choose_letters()
            break
        elif choice == 'Q':
            print("\nExiting game....\n")
            quit()
            break
        else:
            print("Invalid Choice. Input only 'N' or 'Q' ")
            continue        

def one():
    print("  ________   ")
    print(" |       |   ")
    print(" |      ( )  ")
    print(" |           ")
    print(" |           ")
    print(" |           ")
    print(" |           ")
    print(" |           ")
    print("_|_          ")

def two():
    print("  ________   ")
    print(" |       |   ")
    print(" |      ( )  ")
    print(" |       |   ")
    print(" |       |   ")
    print(" |           ")
    print(" |           ")
    print(" |           ")
    print("_|_          ")

def three():
    print("  ________   ")
    print(" |       |   ")
    print(" |      ( )  ")
    print(" |      \|   ")
    print(" |       |   ")
    print(" |           ")
    print(" |           ")
    print(" |           ")
    print("_|_          ")

def four():
    print("  ________   ")
    print(" |       |   ")
    print(" |      ( )  ")
    print(" |      \|/  ")
    print(" |       |   ")
    print(" |           ")
    print(" |           ")
    print(" |           ")
    print("_|_          ")

def five():
    print("  ________   ")
    print(" |       |   ")
    print(" |      ( )  ")
    print(" |      \|/  ")
    print(" |       |   ")
    print(" |      /    ")
    print(" |           ")
    print(" |           ")
    print("_|_          ")
    
def six():
    print("  ________   ")
    print(" |       |   ")
    print(" |      ( )  ")
    print(" |      \|/  ")
    print(" |       |   ")
    print(" |      / \  ")
    print(" |           ")
    print(" |           ")
    print("_|_          ")

 
def choose_letters():
    var='A'
    alphabets=[]
    # starting from the ASCII value of 'a' and keep increasing the 
    # value by i.
    alphabets=[(chr(ord(var)+i)) for i in range(26)]
    print(alphabets)

    word = [
                "AWESOME", 
                "BLESSINGS", 
                "GRATEFUL",
                "REWARDING"
                           ]
    print()
    letters=[]
    tries = 6
    game_over = False
    a=random.choice(word)
    display = '_' * len(a)
    #print(a)
    
    alphabets=[(chr(ord(var)+i)) for i in range(26)]
    
    while not game_over:   
        print()
        print(display)
        print()
        guess = input("Guess a letter: ").upper()

        i = 0
        if guess in a:
            while a.find(guess, i) != -1:
                i = a.find(guess, i)
                display = display[:i] +guess + display[i+1:]
                i += 1
     
        else:   
            while guess not in letters: 
                letters.append(guess)
                print("Selected wrong letters: ", letters)
                tries -=1 
                if tries == 5:
                    one()
                if tries == 4:
                    two()
                if tries == 3:
                    three()
                if tries == 2:
                    four()
                if tries == 1:
                    five()
                if tries == 0:
                    six()
                    print("\nSorry, you are out of attempts.")
                    print("\n------ Game Over ------")
                    menu()
                    break 
                               
        if display == a:
            print()
            print(display)
            print("\nYou Win!")
            menu()  

            
menu()        
        
