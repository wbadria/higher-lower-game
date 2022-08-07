from art import logo, vs
from game_data import data
import random
from replit import clear

# print logo
print(logo)


def format_data(account):
    """Pull up the value associated with each key from the dectionary and make it ready to print
 as name, description, country"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, {account_country}"


def num_of_followers(account):
    """Get the number of followers for each account to compare it later"""
    account_followers = account["follower_count"]
    return account_followers


def check_the_answer(guess, a_followers, b_followers):
    """Compare which account has more followers and check if the user guessed it right or not"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# to track the score
score = 0
# a flag to stop the while loop when user guessed wrong
should_continue = True
# get a random account from the data list from game_data.py file
account_b = random.choice(data)
# while loop to repeat the step while the guess is wright
while should_continue:
    # make account B as A
    account_a = account_b
    # get new random account to compare with the previous account
    account_b = random.choice(data)
    # to make sure we don't get the same account
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # take the user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    clear()
    print(logo)
    # get the number of followers for each account
    a_followers = num_of_followers(account_a)
    b_followers = num_of_followers(account_b)

    # check which account has more and see if user guessed it write
    is_correct = check_the_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
