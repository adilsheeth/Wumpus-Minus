from Modules.Room import Room
from Modules.Item import Item
from Modules.Character import Player, Sentry
import time, os

def main():
    turns = 0
    achievements = {
        "Pacifist": True, # Don't use any EMPs
        "In the dark": True, # Don't use any torches
        "Speedrunner": True # Finish the game in 10 turns
    }
    rooms = {
        "1": Room("Room 1", "1", "You find a torch on the ground.", [Item("Torch", "Illuminates next rooms.", 2)], ["2", "5", "8"]),
        "2": Room("Room 2", "2", "You hear a Sentry in the next room.", [], ["1", "3", "10"]),
        "3": Room("Room 3", "3", "A Sentry spots you.", [Sentry("INTRUDER!!!")], ["2", "4", "12"]),
        "4": Room("Room 4", "4", "You hear a Sentry in the next room.", [], ["3", "5", "14"]),
        "5": Room("Room 5", "5", "You find an EMP on the ground.", [Item("EMP", "Eliminates Sentries", 1)], ["1", "4", "6"]),
        "6": Room("Room 6", "6", "You hear a Sentry in the next room.", [], ["5", "7", "15"]),
        "7": Room("Room 7", "7", "You find a bottle of booze on the ground.", [Item("Booze", "Makes you drunk", 5)], ["6", "8", "17"]),
        "8": Room("Room 8", "8", "You hear a Sentry in the next room.", [], ["1", "7", "9"]),
        "9": Room("Room 9", "9", "A Sentry spots you.", [Sentry("I smell a rat!")], ["8", "10", "18"]),
        "10": Room("Room 10", "10", "You hear a Sentry in the next room.", [], ["2", "9", "11"]),
        "11": Room("Room 11", "11", "You find an EMP on the ground.", [Item("EMP", "Eliminates Sentries", 1)], ["10", "12", "19"]),
        "12": Room("Room 12", "12", "You hear a Sentry in the next room.", [], ["3", "11", "13"]),
        "13": Room("Room 13", "13", "You find a bottle of booze on the ground.", [Item("Booze", "Makes you drunk", 5)], ["12", "14", "20"]),
        "14": Room("Room 14", "14", "You hear a Sentry in the next room.", [], ["4", "13", "15"]),
        "15": Room("Room 15", "15", "A Sentry spots you.", [Sentry("My spidey senses tingle...")], ["6", "14", "16"]),
        "16": Room("Room 16", "16", "You hear a Sentry in the next room.", [], ["15", "17", "20"]),
        "17": Room("Room 17", "17", "You find an EMP on the ground.", [Item("EMP", "Eliminates Sentries", 1)], ["7", "16", "18"]),
        "18": Room("Room 18", "18", "You hear a Sentry in the next room.", [], ["9", "17", "19"]),
        "19": Room("Room 19", "19", "You find a torch on the ground.", [Item("Torch", "Illuminates next rooms.", 2)], ["11", "18", "20"]),
        "20": Room("Room 20", "20", "You find the exit!", [], ["13", "16", "19"])
    }
    
    player = Player("Player", 5, [], rooms["1"])
    while True:
        if os.name == "nt":
            os.system("cls")
        print(f"STATUS\nYou are in room {player.position.id}.")
        turns += 1
        if player.get_boozed():
            print(f"You are drunk for {player.get_boozed_value()} more turns.")
            player.set_boozed(player.get_boozed_value()-1)
        print("\n"+player.position.get_description())
        item = player.get_position().get_items()
        if item != []:
            if isinstance(item, Item):
                player.inventory.append(item)
                player.position.items.remove(item)
                player.position.set_description("There is nothing more in this room.")
            elif isinstance(item, Sentry):
                item.speak()
                print("Engaging Combat!")
                if player.get_boozed():
                    print("You are drunk and manage to talk your way out of the situation. Lucky You.")
                    player.set_enemies_to_kill()
                else:
                    flag = False
                    for thing in player.get_inventory():
                        if thing.get_name() == "EMP":
                            achievements["Pacifist"] = False
                            print("You use the EMP and disable the Sentry. You can now move freely.")
                            player.set_enemies_to_kill()
                            player.inventory.remove(thing)
                            player.position.items.remove(item)
                            flag = True
                            break
                    if not flag:
                        game_over("lose", turns, achievements)
                        break
        if player.get_inventory() == []:
            print("You have no items in your inventory.")
        else:
            print("\nYou have: ")
            for index in range(len(player.get_inventory())):
                print(f"[{index}] {player.get_inventory()[index].name} - ({player.get_inventory()[index].uses} uses)")
            print("")
        if player.position.id == "20":
            if player.get_enemies_to_kill() > 0:
                print("You need to kill all the Sentries before you can exit the base.")
                time.sleep(3)
                player.move(rooms["16"])
                continue
            else:
                game_over("win", turns, achievements)
                break
        print(f"You can go to: {' '.join(player.position.get_links())}")
        while True:
            move = input("What would you like to do? [move, use] ")
            if move == "move":
                i = input("Where would you like to go? ")
                if i in player.position.get_links():
                    player.move(rooms[i])
                    break
                else:
                    print("Invalid room.")
            elif move == "use":
                if player.get_inventory() == []:
                    print("You have no items to use.")
                    break
                else:
                    try:
                        i = int(input("Which item number would you like to use? "))
                    except ValueError:
                        print("Invalid input.")
                    if i < len(player.get_inventory()):
                        if player.inventory[i].get_name() == "Torch":
                            achievements["In the dark"] = False
                            flag = False
                            for z in rooms[player.position.id].get_links():
                                if rooms[z].get_items() != []:
                                    if type(rooms[z].get_items()) == Sentry:
                                        print(f"A Sentry is in room {z}.")
                                        time.sleep(3)
                                        flag = True
                            if not flag:
                                print("No Sentries found.")
                            player.inventory[i].uses -= 1
                            if player.inventory[i].uses == 0:
                                player.inventory.pop(i)
                        elif player.inventory[i].get_name() == "Booze":
                            print("You feel woozy...")
                            time.sleep(2)
                            player.set_boozed(5)
                            player.inventory.pop(i)     
                        elif player.inventory[i].get_name() == "EMP":
                            print("You can't use that now!")
                            time.sleep(2)
                        break
                    else:
                        print("Invalid item number.")

def welcome():
    print("Welcome to Agent's Quest - an interactive adaptation of 'Hunt the Wumpus'!")
    print("You're a secret agent stuck in an underground secret base.")
    print("You must navigate through the base to find the exit. On the way, pick up items, and eliminate Sentries!")
    print("Remember, there are always alternate ways to finish the game...\n")
    if input("Would you like a walk-through of the rules? [y/n] ") == "y":
        print("Along your journey, you will encounter Sentries, who will attack you if you enter their room.")
        print("In order to avoid dying, you need to use items you find in other rooms.")
        print("TORCH: allows you to see what's in adjacent rooms. 2 uses. NOTE: rooms with sentries adjacent will already be marked, but you won't know which room has the sentry without a torch...")
        print("BOOZE: allows you to talk your way out of a Sentry encounter. Lasts for 5 rooms.")
        print("EMP: allows you to disable a Sentry. Single use.")
        input("Press Enter to continue...")
        print("")
    print("Good luck, Agent!\n")

def game_over(status, turns, achievements):
    if status == "win":
        print("Congratulations! You've found the exit!")
        print(f"You made it out in {turns} turns.")
        print("Achievements:")
        for key, value in achievements.items():
            if value:
                print(key)
    else:
        print("You've died. Game Over.")
    if input("Would you like to play again? [y/n] ") == "y":
        print("Starting new game...")
        main()

if __name__ == "__main__":
    welcome()
    main()