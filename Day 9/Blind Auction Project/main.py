# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
new_bids=True
dictionary={}
while new_bids:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    dictionary[name]=bid

    someone_left=input("Are there any other bidders? Type 'yes' or 'no'").lower()

    if someone_left=="no":
        new_bids=False
        for name in dictionary:
            user_with_highest_bid = max(dictionary, key=dictionary.get)
        print(f"The winner is {user_with_highest_bid} with a bid of {dictionary[user_with_highest_bid]}$.")
    else:
        print("\n" * 20)