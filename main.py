import random

def get_winner(player1_choice, player2_choice):
    rules = {
        "rock": {"rock": "tie", "paper": "player2", "scissors": "player1"},
        "paper": {"rock": "player1", "paper": "tie", "scissors": "player2"},
        "scissors": {"rock": "player2", "paper": "player1", "scissors": "tie"},
    }
    return rules[player1_choice][player2_choice]

def get_choice(player_name):
    while True:
        choice = input(f"{player_name}, enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice, please try again.")

def play_round():
    player1_choice = get_choice("Player 1")
    player2_choice = get_choice("Player 2")
    print(f"Player 1 chose: {player1_choice}")
    print(f"Player 2 chose: {player2_choice}")
    winner = get_winner(player1_choice, player2_choice)
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"{winner.capitalize()} wins this round!")
    return winner

def rock_paper_scissors_game():
    player1_score = 0
    player2_score = 0
    rounds = int(input("Enter the number of rounds to play: "))

    for _ in range(rounds):
        winner = play_round()
        if winner == "player1":
            player1_score += 1
        elif winner == "player2":
            player2_score += 1
        print(f"Current Score - Player 1: {player1_score}, Player 2: {player2_score}\n")

    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    rock_paper_scissors_game()
