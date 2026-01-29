from random import randint

# version 1 - no persistance

# secret = randint(0, 500)
# found = False
# guesses = 0
# while not found:
#     guess = int(input("please enter a number between 0-500 "))
#     guesses += 1
#     if guess == secret:
#         print("equal!")
#         found = True
#     elif guess < secret:
#         print("low!")
#     else:
#         print("high!")
# print(f"total guesses: {guesses}")

# version 2 - guess number persistance

# secret = randint(0, 10)
# found = False
# current_guess_num = 0
# with open("./data/guess_number.txt", "r") as f:
#     best_guess_num = int(f.read())
# print("guess num to beat: ", best_guess_num)
# while not found:
#     guess = int(input("please enter a number between 0-500 "))
#     current_guess_num += 1
#     if guess == secret:
#         print("equal!")
#         found = True
#     elif guess < secret:
#         print("low!")
#     else:
#         print("high!")
# print(f"total guesses: {current_guess_num}")
# if best_guess_num > current_guess_num or best_guess_num == 0:
#     with open("./data/guess_number.txt", "w", encoding="utf-8") as f:
#         f.write(str(current_guess_num))

# version 3 - with stop game feature

import time

secret = randint(0, 10)
found = False
current_guess_num = 0
guess = None
computer_answer = None

lines = 0
data_line = None
with open("./data/status.txt", "r") as f:
    for line in f:
        lines += 1
        if lines > 1:
            data_line = line
if lines > 1:
    print("stored game found")
    answer = input("do you want to load it and continue? y/n ")
    if answer.lower() == "y" and data_line is not None:
        splitted_line = data_line.split(",")
        last_date, secret, current_guess_num, guess, computer_answer = splitted_line
        current_guess_num = int(current_guess_num)
        guess = int(guess)
        secret = int(secret)
with open("./data/guess_number.txt", "r") as f:
    best_guess_num = int(f.read())
print("guess num to beat: ", best_guess_num)

while not found:
    to_stop = input("do you want to stop and save? y/n ")
    if to_stop.lower() == "y":
        current_time = time.time()
        with open("./data/status.txt", "a") as f:
            data_line = f"\n{current_time},{secret},{current_guess_num},{guess},{computer_answer}"
            f.write(data_line)
            exit()
    guess = int(input("please enter a number between 0-500 "))
    current_guess_num += 1
    if guess == secret:
        print("equal!")
        computer_answer = "equal!"
        found = True
    elif guess < secret:
        computer_answer = "low"
        print("low!")
    else:
        computer_answer = "high"
        print("high!")
print(f"total guesses: {current_guess_num}")
if best_guess_num > current_guess_num or best_guess_num == 0:
    with open("./data/guess_number.txt", "w", encoding="utf-8") as f:
        f.write(str(current_guess_num))
