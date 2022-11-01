class Faction:
    #Constructor
    def __init__(self,name = "Default",units_num = 50,attack_point = 30,health_point = 150,unit_reg_num = 10):
        #Assign parameters to attributes.
        self.name = name
        self.units_num = units_num
        self.attack_point = attack_point
        self.health_point = health_point
        self.unit_reg_num = unit_reg_num
        #Assign enemies attributes.
        self.first_enemy = None
        self.second_enemy = None
        #Set total health value and alive status.
        self.total_health = self.units_num * self.health_point
        self.alive_status = True
    #Method to update total health.
    def set_total_health(self):
        self.total_health = self.units_num * self.health_point
    #Methods(These below 5 methods will be overriden by child classes)
    def assign_enemies(self):
        pass
    def perform_attack(self):
        pass
    def receive_attack(self,attacker,damage):
        pass
    def purchase_weapons(self):
        pass
    def purchase_armors(self):
        pass
    #Print the information about faction.
    def print(self):
        alive_stat = "Alive" if self.alive_status else "Defeated"
        print(f"Faction name : {self.name}\nStatus : {alive_stat}\nNumber of Units : {self.units_num}\n"
              f"Attack Point : {self.attack_point}\nHealth Point : {self.health_point}\n"
              f"Unit Regen Number : {self.unit_reg_num}\nTotal Faction Health : {self.total_health}\n")
    #End turn
    def end_turn(self):
        if self.units_num < 0:
            self.units_num = 0
        if self.units_num == 0:
            self.alive_status = False
        self.set_total_health()

