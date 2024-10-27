import random
import art
from game_data import data


def comparison(a_to_compare, b_to_compare):
    if a_to_compare > b_to_compare:
        return "A"
    else:
        return "B"

def game():
    #generate data
    is_game_over = False
    current_score = 0
    a = random.choice(data)  # return dictionary
    a_full_data = a["name"] + ", a " + a["description"] + ", from " + a["country"]
    a_followers = int(a["follower_count"])
    while not is_game_over:
        print(art.logo)
        # a = random.choice(data)  # return dictionary
        # a_full_data = a["name"] + ", a " + a["description"] + ", from " + a["country"]
        # a_followers = int(a["follower_count"])
        b = random.choice(data)

        while a == b:
            b = random.choice(data)
        b_full_data = b["name"] + ", a " + b["description"] + ", from " + b["country"]
        b_followers = int(b["follower_count"])

        print(f"Compare A: {a_full_data}")
        print(art.vs)
        print(f"Against B: {b_full_data}")
        correct_answer = comparison(a_followers, b_followers)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice==correct_answer:
            current_score+=1
            print(f"You are right!. Current score is {current_score}.")
        if correct_answer == "B":
            a = b
            a_full_data = b_full_data
            a_followers=b_followers
        else:
            print(f"You are wrong! You lose. Your final score was {current_score}.")
            is_game_over = True

game()