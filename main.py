import random
import time

suite_data = {1: "Suite No. 1 in G major, BWV 1007", 2: "Suite No. 2 in D minor, BWV 1008",
              3: "Suite No. 3 in C major, BWV 1009",
              4: "Suite No. 4 in E♭ major, BWV 1010", 5: "Suite No. 5 in C minor, BWV 1011",
              6: "Suite No. 6 in D major, BWV 1012"}

movement_data = {1: "Prelude", 2: "Allemande", 3: "Courante", 4: "Sarabande", 5: "Minuet I / II", 6: "Gigue"}


def initial_instructs(name):
    print(f'Hi, {name} welcome to the Bach randomizer!\n')
    initial_input = input("Ready to roll? (y/n): ")
    print("\n")
    return initial_input


def select_random():
    suite_key, random_suite = random.choice(list(suite_data.items()))
    movement_key, random_movement = random.choice(list(movement_data.items()))

    if (suite_key == 3 or suite_key == 4) and movement_key == 5:
        return random_suite + ": Bourrée I / II"

    if (suite_key == 5 or suite_key == 6) and movement_key == 5:
        return random_suite + ": Gavotte I / II"

    return random_suite + ": " + random_movement


def reroll():
    response = input("Reroll? (y/n): ")
    print("\n")
    return response


def farewell():
    print("Thanks for playing! Goodbye! <3")
    time.sleep(2)
    quit()


if __name__ == '__main__':
    program_beginning = initial_instructs('Rebecca')
    if program_beginning != "y":
        farewell()

    else:

        while True:
            print(select_random())
            user_response = reroll()
            if user_response != "y":
                break
        farewell()
