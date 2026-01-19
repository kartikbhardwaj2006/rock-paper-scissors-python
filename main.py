import random

choices_map = {
    "rock": 1,
    "paper": -1,
    "scissors": 0
}

reverse_map = {
    1: "Rock",
    -1: "Paper",
    0: "Scissors"
}

user_score = 0
computer_score = 0

while True:
    computer_choice = random.choice([1, -1, 0])
    user_input = input("\nEnter Rock, Paper, Scissors or type 'exit' to quit: ").lower()

    if user_input == "exit":
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break

    user_choice = choices_map.get(user_input)

    if user_choice is None:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
        continue

    print(f"\nYou chose {reverse_map[user_choice]} and the Computer chose {reverse_map[computer_choice]}.")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == -1 and computer_choice == 1) or
        (user_choice == 0 and computer_choice == -1)
    ):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")
