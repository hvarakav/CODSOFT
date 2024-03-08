import random

def rematch_prompt():
  """Asks the user if they want another round. 

  Returns:
      bool: True if the user wants to play again, False otherwise.
  """
  while True:
    answer = input("Ready for another round? (y/n): ").lower()
    if answer in ("y", "yes"):
      return True
    elif answer in ("n", "no"):
      return False
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

def valid_move(choice):
  """Checks if the user's choice is valid (rock, paper, or scissors).

  Args:
      choice: The user's choice.

  Returns:
      bool: True if the choice is valid, False otherwise.
  """
  return choice.lower() in ("rock", "paper", "scissors")

def decide_victor(user_choice, computer_choice):
  """Determines the winner of the game based on user and computer choices.

  Args:
      user_choice: The user's choice.
      computer_choice: The computer's choice.

  Returns:
      str: "Victory", "Defeat", or "Tie" depending on the winner.
  """
  options = ["rock", "paper", "scissors"]
  user_index = options.index(user_choice.lower())
  computer_index = options.index(computer_choice.lower())

  # Check for tie
  if user_index == computer_index:
    return "Tie"

  # Check for win/loss based on rock-paper-scissors logic (shifted by 1)
  if (user_index + 1) % 3 == computer_index:
    return "Victory"
  else:
    return "Defeat"

def main_game():
  """Runs the main game loop."""
  user_score = 0
  computer_score = 0

  while True:
    print("Rock-Paper-Scissors!")

    # User input
    while True:
      user_choice = input("Enter your move (rock, paper, scissors): ")
      if valid_move(user_choice):
        break
      else:
        print("Invalid move. Please enter rock, paper, or scissors.")

    # Computer selection
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine winner and display results
    result = decide_victor(user_choice, computer_choice)
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    if result == "Victory":
      print("You win!")
      user_score += 1
    elif result == "Defeat":
      print("You lose.")
      computer_score += 1
    else:
      print("It's a tie!")

    print(f"Your score: {user_score}, Computer score: {computer_score}")

    # Play again prompt
    if not rematch_prompt():
      break

  print("Thanks for playing!")

if __name__ == "__main__":
  main_game()