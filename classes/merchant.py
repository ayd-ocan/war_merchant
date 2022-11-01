from classes.faction import Faction
from classes.orcs_dwarves_elves import *
class Merchant:
    #Consturctor.
    def __init__(self,starting_weapon_point = 10,starting_armor_point = 10):
        #Staring points.
        self.start_weapon_point = starting_weapon_point
        self.start_armor_point = starting_armor_point
        #Revenue
        self.revenue = 0
        #Weapon and armor points left for day.
        self.weapon_point = starting_weapon_point
        self.armor_point = starting_armor_point
    #Assign factions.
    def assign_factions(self):
        # Factions
        self.first_faction = Orcs("Orcs", 50, 60, 150, 10)
        self.second_faction = Dwarves("Dwarves", 50, 70, 150, 10)
        self.third_faction = Elves("Elves", 50, 30, 50, 10)
        return self.first_faction,self.second_faction,self.third_faction
    #Sell weapons
    def sell_weapons(self,buyer):
        #Get the weapon point.
        sell_w_point = int(input("Enter the amount of weapons which you want to sell : \n"))
        #If everything is okey,sold weapon.
        if(sell_w_point <= self.weapon_point and buyer.alive_status == True):
            print("Weapons sold!\n")
            self.weapon_point -= sell_w_point
            #Increase revenue with golds respect to buyer.
            self.revenue += buyer.purchase_weapons(sell_w_point)
            return True
        #If buyer faction is dead,return false.
        elif (buyer.alive_status == False):
            print("The faction you want to sell weapon is dead!\n")
            return False
        #If you dont have enough weapon points to sell,return False.
        elif (sell_w_point > self.weapon_point):
            print("You try to sell more weapons than you have in possession.\n")
            return False
        #Any other cases,return False.
        else:
            return False
    #Sell armors method.
    def sell_armors(self,buyer):
        sell_a_point = int(input("Enter the amount of armor you want to sell : \n"))
        # If everything is okey,sold armors.
        if (sell_a_point <= self.armor_point and buyer.alive_status == True):
            print("Armors sold!\n")
            self.armor_point -= sell_a_point
            # Increase revenue with golds respect to buyer.
            self.revenue += buyer.purchase_armors(sell_a_point)
            return True
        # If buyer faction is dead,return false.
        elif (buyer.alive_status == False):
            print("The faction you want to sell armors is dead!\n")
            return False
        # If you dont have enough armor points to sell,return False.
        elif (sell_a_point > self.armor_point):
            print("You try to sell more armors than you have in possession.\n")
            return False
        # Any other cases,return False.
        else:
            return False

    #End turn method.
    def end_turn(self):
        self.weapon_point = self.start_weapon_point
        self.armor_point = self.start_armor_point
        #Use faction end turn method to update alive status.
        self.first_faction.end_turn()
        self.second_faction.end_turn()
        self.third_faction.end_turn()
        print(f"Your revenue is : {self.revenue}")


