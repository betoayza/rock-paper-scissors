import random

def validate_choice(choice = 1):   
    isOk = False 
    while not isOk:
        try:
            choice = int(input("""\nPlease, select the number:
                1.  Rock.
                2.  Paper.
                3.  Scissors
                4.  Exit
                """))
            if choice <1 or choice>4:
                print("Ha, that's not an option!")
                continue
            isOk = True
            return choice
        except ValueError:
            print("Ha, that's not an option!")    

#----------------
print("Welcome to Rock Paper Scissors!")

options_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}
player_wins = 0
machine_wins = 0 

choice = validate_choice()

while choice != 4:    
    machine_choice = random.randint(1,3)
    
    print("\nYour choice is: ", options_dict[choice])
    print("Machine choice is: ", options_dict[machine_choice])

    round = [choice, machine_choice]

    if choice == machine_choice:
        print("\nThere is draw! Next round... ")
    # si gana jugador
    if round == [1, 3] or round == [2, 1] or round == [3, 2]:
        player_wins += 1
        print("\nYou win this round!")
    # si pierde jugador
    if round == [1, 2] or round == [2, 3] or round == [3, 1]:
        machine_wins += 1
        print("\nYou lost this round...")    
    
    print("\n   Marker is:", [player_wins, machine_wins])

    if player_wins == 3 or machine_wins == 3:
        break
    else:
        print("\nNext round...")
        choice = validate_choice()

if player_wins == 3 or machine_wins == 3:
    print("\n*** You won the game, your are awesome!") if player_wins > machine_wins else print("\n*** Machine won! Good look next time...")
else:
    print("\n*** You are a coward, get out of here!")


