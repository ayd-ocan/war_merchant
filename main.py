from classes.orcs_dwarves_elves import *
from classes.merchant import *
import random


#Menu function.
def menu():
    choice = int(input("(1)See the information of factions\n(2)Sell weapons and armors\n(3)End turn\n(4)Quit game\n"))
    return choice

#See informations about factions function.
def info_factions(orcs,dwarves,elves):
    orcs.print()
    dwarves.print()
    elves.print()
#Sell weapons and armors function.
def sell_weapons_armors(c):
    # Choose buyer and sell weapon if its okey.
    buyer = int(input("(1)to Orcs\t(2)to Dwarves\t(3)to Elves\n"))
    if(c == 1):
        merchant.sell_weapons(factions[buyer-1])
    elif(c == 2):
        merchant.sell_armors(factions[buyer-1])
    else:
        print("Undefined operation")
#Check if alive status of factions and decide the winner.
def check_alive_status_factions(factions):
    if(factions[0].alive_status == True and factions[1].alive_status == False and factions[2].alive_status == False):
        print(f"Game is over.Winner is {factions[0].name}")
        return False
    elif(factions[0].alive_status == False and factions[1].alive_status == True and factions[2].alive_status == False):
        print(f"Game is over.Winner is {factions[1].name}")
    elif(factions[0].alive_status == False and factions[1].alive_status == False and factions[2].alive_status == True):
        print(f"Game is over.Winner is {factions[2].name}")
    else:
        return True


if __name__ == '__main__':
    print("Welcome the war merchant!")
    #Define merchant with weapon and armor stocks,and assign factions.
    merchant = Merchant(20,20)
    orcs,dwarves,elves = merchant.assign_factions()
    factions = [orcs,dwarves,elves]
    #Assign enemies for all factions.
    orcs.assign_enemies(elves,dwarves)
    dwarves.assign_enemies(orcs,elves)
    elves.assign_enemies(orcs,dwarves)

    while(True):
        choice = menu()
        #If choice == 1,print all information about factions.
        if(choice == 1):
            info_factions(orcs,dwarves,elves)
        #If choice == 2,sell weapons and armors.
        elif(choice == 2):
            c = int(input("(1)Sell weapon\n(2)Sell armor\n"))
            sell_weapons_armors(c)
        #If choice == 3 ,end turn.
        elif(choice == 3):
            #Check alive status of factions.
            all_status = check_alive_status_factions(factions)
            #If all factions are alived.
            if(all_status == True):
                #Randomly chosen attack from one faction to others.
                idx = random.randint(0,2)
                if (factions[idx].alive_status == True):
                    factions[idx].perform_attack()
                else:
                    print("Dead faction cannot attack!")
                # End turn for merchant.
                merchant.end_turn()
            #Game over.
            else:
                print(f"Your final revenue is : {merchant.revenue}")
                break

        #If choice == 4,quit the game.
        elif(choice == 4):
            print("See you next time!")
            break
        else:
            print("Undefined operation.")