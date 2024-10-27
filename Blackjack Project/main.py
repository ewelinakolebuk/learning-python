import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:
    play_or_not=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_or_not == "y":
        user_hand = [random.choice(cards), random.choice(cards)]
        user_score = sum(user_hand)
        computer_hand = [random.choice(cards), random.choice(cards)]
        computer_score = sum(computer_hand)
        print(f"Your card: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while another_card=="y":
            user_hand.append(random.choice(cards))
            user_score = sum(user_hand)
            if user_score > 21 and 11 in user_hand:
                user_hand[user_hand.index(11)] = 1
                user_score = sum(user_hand)

            computer_hand = [random.choice(cards), random.choice(cards)]
            computer_score = sum(computer_hand)
            if computer_score<16:
                computer_hand.append(random.choice(cards))
                computer_score = sum(computer_hand)
                if computer_score>21 and 11 in computer_hand:
                    computer_hand[computer_hand.index(11)]=1
                    computer_score = sum(computer_hand)
            if user_score > 21 or computer_score>21:
                another_card = "n"
                break
            print(f"Your card: {user_hand}, current score: {user_score}")
            print(f"Computer's first card: {computer_hand[0]}")

            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card=="n":
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            if user_score == computer_score:
                print("It is a draw!")
            elif user_score > 21:
                print("You went over. Opponent wins!")
            elif computer_score>21:
                print("Opponent went over. You win!")
            elif user_score>computer_score:
                print("You win!")
            elif computer_score>user_score:
                print("You lose!")
    elif play_or_not == "n":
        print("Bye!")
        break

