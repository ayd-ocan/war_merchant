from classes.faction import Faction
#1.2 Orcs class
class Orcs(Faction):
    #Uses parent class constructor.
    def __init__(self,name = "Default",units_num = 50,attack_point = 30,health_point = 150,unit_reg_num = 10):
        super().__init__(name,units_num,attack_point,health_point,unit_reg_num)

    #Assign enemies function.
    def assign_enemies(self,elves,dwarves):
        self.first_enemy = elves
        self.second_enemy = dwarves
    #Perform attack method.
    def perform_attack(self):
        #(1)If one enemy alive,attack it with all units.
        #(Use receive attack method of enemies in below)
        #Attack first enemy
        if(self.first_enemy.alive_status == True and self.second_enemy.alive_status == False):
            damage = self.attack_point * self.units_num
            self.first_enemy.receive_attack(self.name,damage)
        #Attack second enemy.
        elif(self.first_enemy.alive_status == False and self.second_enemy.alive_status == True):
            damage = self.attack_point * self.units_num
            self.second_enemy.receive_attack(self.name,damage)
        #(2)If both are alive,attack elves with %70,attack dwarves with %30.
        elif(self.first_enemy.alive_status == True and self.second_enemy.alive_status == True):
            damage1 = self.units_num * 0.7 * self.attack_point
            damage2 = self.units_num * 0.3 * self.attack_point
            self.first_enemy.receive_attack(self.name,damage1)
            self.second_enemy.receive_attack(self.name,damage2)
        else:
            pass
    #Receive attack method.
    def receive_attack(self,attacker,damage):
        #Follow the instructions from assigment with respect to type of attacker.
        if(attacker == "Elves"):
            self.units_num = self.units_num - ((damage * 0.75) / self.health_point)
            self.total_health = self.units_num * self.health_point
        elif(attacker == "Dwarves"):
            self.units_num = self.units_num -((damage  * 0.8) / self.health_point)
            self.total_health = self.units_num * self.health_point
        else:
            pass
    #Purchase weapons method.
    def purchase_weapons(self,amount):
        #Increase attack point with double of weapons.
        self.attack_point += amount * 2
        #Give 20 gold for each weapon to merchant.
        return 20 * amount
    #Purchase armors method.
    def purchase_armors(self,amount):
        #Increase health ponit with triple of armors.
        self.health_point += amount * 3
        #Give 1 gold for each armor to merchant.
        return amount * 1
    #Print information method.
    def print(self):
        print("Stop running,you'll only die tired!")
        super().print()

#1.3 Dwarves Class
class Dwarves(Faction):
    # Uses parent class constructor.
    def __init__(self, name="Default", units_num=50, attack_point=30, health_point=150, unit_reg_num=10):
        super().__init__(name, units_num, attack_point, health_point, unit_reg_num)

    #Assign enemies function.
    def assign_enemies(self,orcs,elves):
        self.first_enemy = orcs
        self.second_enemy = elves
    #Perform attack method .
    def perform_attack(self):
        # (1)If one enemy alive,attack it with all units.
        # (Use receive attack method of enemies in below)
        # Attack only first enemy
        if(self.first_enemy.alive_status == True and self.second_enemy.alive_status == False):
            damage = self.units_num * self.attack_point
            self.first_enemy.receive_attack(self.name,damage)
        #Attack only second enemy.
        elif(self.first_enemy.alive_status == False and self.second_enemy.alive_status == True):
            damage = self.units_num * self.attack_point
            self.second_enemy.receive_attack(self.name,damage)
        #Attack both of them.
        elif(self.first_enemy.alive_status == True and self.second_enemy.alive_status == True):
            damage1 = self.units_num * self.attack_point * 0.5
            damage2 = self.units_num * self.attack_point * 0.5
            self.first_enemy.receive_attack(self.name,damage1)
            self.second_enemy.receive_attack(self.name,damage2)
        else:
            pass
    #Receive attack method.
    def receive_attack(self,attacker,damage):
        # Follow the instructions from assignment with respect to type of attacker.
        self.units_num = self.units_num -(damage / self.health_point)
        self.total_health = self.units_num * self.health_point

    #Purchase weapons method.
    def purchase_weapons(self,amount):
        # Increase attack point with weapons.
        self.attack_point += amount
        # Give 10 gold for each weapon to merchant.
        return 10 * amount
    #Purchase armors method.
    def purchase_armors(self,amount):
        # Increase health point with double of armors.
        self.health_point += amount * 2
        # Give 20 gold for each weapon to merchant.
        return 3 * amount
    #Print information method.
    def print(self):
        print("Taste the power of our axes!")
        super().print()


#1.4 Elves class
class Elves(Faction):
    # Uses parent class constructor.
    def __init__(self, name="Default", units_num=50, attack_point=30, health_point=150, unit_reg_num=10):
        super().__init__(name, units_num, attack_point, health_point, unit_reg_num)

    def assign_enemies(self,orcs,dwarves):
        self.first_enemy = orcs
        self.second_enemy = dwarves
    #Perform attack method
    def perform_attack(self):
        # (1)If one enemy alive,attack it with all units.
        # (Use receive attack method of enemies in below)
        # Attack only first enemy
        if (self.first_enemy.alive_status == True and self.second_enemy.alive_status == False):
            damage = self.units_num * self.attack_point
            self.first_enemy.receive_attack(self.name, damage)
        # Attack only second enemy(to dwarves,increase attack point to %150)
        elif (self.first_enemy.alive_status == False and self.second_enemy.alive_status == True):
            damage = self.units_num * self.attack_point * 1.5
            self.second_enemy.receive_attack(self.name, damage)
        # Attack both of them.(Attack orcs with %60,attack dwarves with %40)
        elif (self.first_enemy.alive_status == True and self.second_enemy.alive_status == True):
            damage1 = self.units_num * self.attack_point * 0.6
            damage2 = self.units_num * self.attack_point * 0.4
            self.first_enemy.receive_attack(self.name, damage1)
            self.second_enemy.receive_attack(self.name, damage2)
        else:
            pass

    # Receive attack method.
    def receive_attack(self, attacker, damage):
        # Follow the instructions from assignment with respect to type of attacker.
        if (attacker == "Orcs"):
            self.units_num = self.units_num -((damage * 1.25) / self.health_point)
            self.total_health = self.units_num * self.health_point
        elif (attacker == "Dwarves"):
            self.units_num = self.units_num - ((damage * 0.75) / self.health_point)
            self.total_health = self.units_num * self.health_point
        else:
            pass
    #Purchase weapon method.
    def purchase_weapons(self,amount):
        # Increase attack point with double of weapons.
        self.attack_point += amount * 2
        # Give 15 gold for each weapon to merchant.
        return 15 * amount
    #Purchase armor method.
    def purchase_armors(self,amount):
        # Increase health point with quadruple of weapons.
        self.health_point += amount * 4
        # Give 5 gold for each weapon to merchant.
        return 5 * amount
    #Print method.
    def print(self):
        print("You cannot reach our elegance.")
        super().print()
