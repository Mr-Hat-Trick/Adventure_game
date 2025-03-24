import random
import character as ch


def room1(character):
    print(
        f"Welcome to the beginning of the game {character.name}.\nYou will be given a series of tasks to complete to continue on to the next rooms.\n"
        f"Fail to complete the tasks, and you will be stuck here forever. For your first task, you have to guess a rando number between 11 and 18.")

    random_num = random.randint(11, 18)

    solved = False

    # Start game
    while not solved and character.health > 0:
        user_num = int(input("Enter your number: "))
        if user_num == random_num:
            print("You guessed correctly")
            solved = True
            if character.health == 150:
                character.add_to_health(10)
            else:
                character.add_to_health(10)
        elif user_num > random_num:
            print("Your guess is greater than the correct value")
            character.remove_health(25)
            print(character)
        elif user_num < random_num:
            print("You guessed lower than the correct value")
            character.remove_health(25)

    if character.health <= 0:
        print("GAME OVER!!!")
        exit()
    else:
        print("Congrats, you've moved onto to the next room")
        print(f"Health:{character.health}")


def room2(character):
    print("Congratulations, most people don't even make it past the first room. It only gets harder from here.\n"
          f"In this room you will have to fight a beast and make it out of here alive. You have 3 differetn strikes to choose from. Jiu-Jitsu, Wrestling, and Muay Thai. Good luck.")
    strikes = ["Jiu-Jitsu", "Wrestling", "Muay Thai"]
    Beast = ch.Character("Beast", 100)

    user_choice = input("Choose your strike:")

    if user_choice.lower() == "jiu-jitsu":
        character.add_f_style(30)
    elif user_choice == "Wrestling":
        character.add_f_style(20)
    elif user_choice == "Muay Thai":
        character.add_f_style(10)

    # Fight loop starts
    turn = 1
    while character.health > 0 and Beast.health > 0:

        print(character)
        print(Beast)
        print(f"Turn {turn}")
        u_flag = input("Ready to roll?")
        if u_flag.lower() == "y":
            roll = random.randint(1, 20)

            if roll <= 20 and roll > 15:
                Beast.remove_health(character.fighting_style)
            elif roll < 5:
                print("Beast defended!")
            else:
                if Beast.health > 0:
                    turn += 1


def room3(character):
    print("You're a strong one, lets see if you can make it out of this room and win the game.\n"
          f"There's 3 cups, one of them has a prize inside. You have to guess which cup has the prize in it. But, the cups will shuffle every time you guess. Good luck.")
    cups = ["Red", "Blue", "Orange"]
    print(cups)
    solved = False
    while solved is False:
        prize_cup = random.choice(cups)
        user_guess = input("Which cup has the prize in it? Choose wisely...")
        if user_guess.lower() == prize_cup:
            print("Wow, I didn't think you would guess correctly. You win the game, you are the chosen one!")
            solved = True
        else:
            print("You guessed wrong, try again. No pressure...")
            character.remove_health(15)
            print(f"Health:{character.health}")
        if character.health <= 0:
            print("GAME OVER!!!")
            exit()