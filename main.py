import rpg

kitchen = rpg.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description("The biggest room in this house. Large and magnificent")

ballroom = rpg.Room("Ballroom")
ballroom.set_description("Centuries ago it was beautifull")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")


cheese = rpg.Item("cheese", "legendary")
cheese.set_description("yellow round cheese. smels tasty")
kitchen.set_item(cheese)

sword = rpg.Item("sword", "common")
sword.set_description("standart boring sword")
ballroom.set_item(sword)

stick = rpg.Item("stick", "rare")
stick.set_description("Bob's stick. Another useless trofey")

dave = rpg.Enemy("Dave", "A smelly zombie")
dave.set_conversation("I'm hungry. Could you give me your brains, please?")
dave.set_weakness(cheese)
dining_hall.set_character(dave)


bob = rpg.Enemy("Bob", "giant shy troll")
bob.set_conversation("Don't look at me")
bob.set_weakness(sword)
bob.set_loot(stick)
kitchen.set_character(bob)


laura = rpg.Friend("Laura", "Sad Sceleton")
laura.set_conversation("I'm so tired")
laura.set_feeling("bad")
ballroom.set_character(laura)


backpack = []
current = kitchen
roomchanged = True
while current.enemies>0:
    if roomchanged:
        current.get_details()
        roomchanged = False
    inhabitant = current.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input('> ')
    if command in ['west','east','north','south']:
        current = current.move(command)
        roomchanged = True
    elif command == 'talk':
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one to talk with here")
    elif command == 'fight':
        if (inhabitant is not None) and (inhabitant.alive) and (isinstance(inhabitant, rpg.Enemy)):
            if backpack:
                battle_item = input("what would you like to fight with?\n")
                while battle_item not in [x.name for x in backpack]:
                    battle_item = input("There is no such item in your backback.\n What would you like to fight with?\n")
            else:
                break
            isbattlewon = inhabitant.fight(battle_item)
            if not isbattlewon:
                break
            else:
                current.enemydefeat()
        else:
            print("There is no one to fight with here")
    elif command == 'steel':
        if (inhabitant is not None) and (inhabitant.alive) and (isinstance(inhabitant, rpg.Enemy)):
            if not inhabitant.steel(backpack):
                break
            else:
                if not inhabitant.alive:
                    current.enemydefeat()
        else:
            print("Nothing to steel here")
    elif command == 'hug':
        if (inhabitant is not None)and(isinstance(inhabitant, rpg.Friend)):
            inhabitant.hug()
        else:
            print("There is no one friend here")
    elif command =="take":
        cur_item = current.get_item()
        if cur_item is not None:
            backpack.append(cur_item)
            print("You have picked "+cur_item.name)
        else:
            print("There is nothing to take here")
print("Victory!")
