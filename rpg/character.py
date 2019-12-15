from random import randint
class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.alive = True

    # Describe this character
    def describe(self):
        if self.alive:
            print( self.name + " is here!" )
            print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.alive:
            if self.conversation is not None:
                print("[" + self.name + " says]: " + self.conversation)
            else:
                print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        if self.alive:
            print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.loot = None
    
    def set_loot(self, loot):
        self.loot = loot

    def get_loot(self):
        return self.loot

    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness
    
    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness.name:
            print("You killed "+self.name+" with "+combat_item)
            self.alive = False
            return True
        else:
            print("You were killed by "+self.name)
            return False
    
    def steel(self, backpack):
        if self.loot is None:
            print("Pointless. Nothing to steel")
            return True
        else:
            if randint(1,2) == 1:
                print("you have stolen "+self.loot.name+"!")
                backpack.append(self.loot)
                self.loot = None
                return True
            else:
                print("Bad luck. You have to fight now")
                if backpack:
                    combat_item = input("What whould you like to fight with?\n")
                    while combat_item not in [x.name for x in backpack]:
                        combat_item = input("There is no such item in your backback.\n What would you like to fight with?\n")
                else:
                    return False
                if self.fight(combat_item):
                    self.loot = None
                    self.alive = False


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name,char_description)
        self.feeling = None
        self.likeshugs = True

    def set_feeling(self, feeling):
        self.feeling = feeling

    def get_feeling(self):
        return self.feeling

    def set_likeshugstoFalse(self):
        self.likeshugs = False

    def hug(self):
        if self.likeshugs:
            print("["+self.name+"]: oh, that's so sweet")
            self.feeling = "good"
        else:
            print("Sorry, I don't like hugs")