import random

if __name__ == "__main__":
    continue_play = True
    choices = ["r", "p", "s"]

    while continue_play:
        computer_points = 0
        human_points = 0
        print("Lets play Rock Paper Scissors")
        while human_points < 3 and computer_points < 3:
            user_input_valid = False
            user_input = input("choose r for rock, p for paper, s for scissors: ")
            user_input_valid = user_input in choices
            while not user_input_valid:
                user_input = input("try again... choose r for rock, p for paper, s for scissors: ")

            computer_choice = random.choice(choices)
            if  \
                (user_input is 'r' and computer_choice is 's')\
                or \
                (user_input is 'p' and computer_choice is 'r')\
                or \
                (user_input is 's' and computer_choice is 'p'):
                human_points += 1
            elif user_input is computer_choice:
                pass
            else:
                computer_points += 1

        print(f"the winnder is {'computer' if computer_points == 3 else 'human'}")
        user_input = input('would you like to keep playing? y for yes, anything else for no')
        if user_input != 'y':
            continue_play = False
