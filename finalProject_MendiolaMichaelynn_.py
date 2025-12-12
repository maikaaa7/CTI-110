# Michaelynn Mendiola
# 12/12/2025
# Final Project
# A text-based game

import random
import time

def create_character():
    """Value returning function to create a new character."""
    name = input("Enter cat's name: ")
    health = int(input(f"Enter {name}'s health: "))
    strength = int(input(f"Enter {name}'s strength: "))

    inventory = {
        "fish": 2,
        "catnip": 1,
        "bandage": 1
    }

    character = {
        'name': name,
        'health': health,
        'strength': strength,
        'inventory': inventory
    }

    print(f"{name} has been created 🐱")
    time.sleep(0.5)
    return character


def display_characters(characters):
    """Non-value returning function to display all characters."""
    print("🌼 🌻 🌷 🌼 🌻 🌷")
    print("------------ALL CATS----------")

    for char in characters:
        print(f"Name: {char['name']}, Health: {char['health']}, Strength: {char['strength']}")
        print(f"Inventory: {char['inventory']}")
        print("-----------------------------")
        time.sleep(0.3)


def attack(attacker, defender):
    """Value-returning function to perform an attack and return the defender's updated health."""
    print(f"\n{attacker['name']} prepares to attack...")
    time.sleep(0.7)

    damage = random.randint(0, attacker['strength'])
    defender['health'] -= damage

    print(f"{attacker['name']} attacks {defender['name']}! 🐾")
    print(f"Damage done: {damage}")
    time.sleep(0.5)
    return defender['health']


def use_item(character):
    """Allows a character to use an item from their inventory."""
    print(f"\n{character['name']}'s Inventory: {character['inventory']}")
    item = input("Choose an item to use (fish/catnip/bandage): ")

    if item not in character['inventory'] or character['inventory'][item] == 0:
        print("❌ Item not available!")
        return

    if item == "fish":
        character['health'] += 5
        print(f"{character['name']} ate a fish and gained 5 health! 🐟")
    elif item == "catnip":
        character['strength'] += 2
        print(f"{character['name']} used catnip and gained +2 strength! 🌿")
    elif item == "bandage":
        character['health'] += 10
        print(f"{character['name']} used a bandage and healed 10 health! 🩹")

    character['inventory'][item] -= 1
    time.sleep(0.5)


def random_event(character):
    """Triggers a random event that affects the cat."""
    events = [
        "found fish",
        "found bandage",
        "catnip boost",
        "fell in mud",
        "wild dog chase"
    ]

    event = random.choice(events)

    print(f"\n🌟 RANDOM EVENT for {character['name']}...")
    time.sleep(0.6)
    print(f"{character['name']} {event}! 🌟")
    time.sleep(0.6)

    if event == "found fish":
        character['inventory']["fish"] += 1
        print(f"{character['name']} found a fish! (+1 fish 🐟)")
    elif event == "found bandage":
        character['inventory']["bandage"] += 1
        print(f"{character['name']} found a bandage! (+1 bandage 🩹)")
    elif event == "catnip boost":
        character['strength'] += 3
        print(f"{character['name']} feels powerful! (+3 strength 🌿)")
    elif event == "fell in mud":
        character['health'] -= 4
        print(f"{character['name']} slipped in mud (-4 health 😿)")
    elif event == "wild dog chase":
        character['health'] -= 7
        print(f"{character['name']} was chased by a dog! (-7 health 🐶)")

    time.sleep(0.5)


def choose_character(characters):
    """Allows player to select a character to control."""
    print("\nChoose your main cat:")
    for i, char in enumerate(characters, start=1):
        print(f"{i}. {char['name']}")

    choice = int(input("Enter number: "))
    return characters[choice - 1]


def main():
    print("🐾 Welcome to CAT QUEST 🐾")
    time.sleep(0.5)

    # Create characters
    wizard_cat = create_character()
    knight_cat = create_character()
    hunter_cat = create_character()

    characters = [wizard_cat, knight_cat, hunter_cat]

    # Select your main character
    player = choose_character(characters)

    print(f"\n🎉 You are now playing as {player['name']}!")
    time.sleep(0.6)

    # MENU SYSTEM (GAME LOOP)
    while True:
        print("\n----- MENU -----")
        print("1. Display all characters")
        print("2. Attack another cat")
        print("3. Use an item")
        print("4. Random event")
        print("5. Quit game")
        choice = input("Choose an option: ")

        if choice == "1":
            display_characters(characters)

        elif choice == "2":
            print("\nChoose a cat to attack:")
            for i, cat in enumerate(characters, start=1):
                if cat != player:
                    print(f"{i}. {cat['name']}")

            defender_index = int(input("Enter number: ")) - 1
            defender = characters[defender_index]

            if defender == player:
                print("❌ You cannot attack yourself!")
            else:
                attack(player, defender)

        elif choice == "3":
            use_item(player)

        elif choice == "4":
            random_event(player)

        elif choice == "5":
            print("Thanks for playing Cat Quest! 🐾")
            break

        else:
            print("Invalid option, try again!")


main()