import character as ch

import rooms as r

if __name__ == "__main__":
    username = input("Please enter your username: ")
    main_character = ch.Character(username, 150)
    print(main_character)

    r.room1(main_character)

    r.room2(main_character)

    r.room3(main_character)
