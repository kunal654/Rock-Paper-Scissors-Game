

# Rock-Paper-Scissors Game

This Python script implements a simple Rock-Paper-Scissors game where two players take turns choosing between rock, paper, or scissors. The winner of each round is determined based on the classic rules of Rock-Paper-Scissors.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Player Interaction**: Allows two players to input their choices for each round.
- **Classic Rules**: Follows the standard rules of Rock-Paper-Scissors to determine the winner of each round.
- **Score Tracking**: Keeps track of the score for each player throughout the game.
- **Customizable Rounds**: Allows the number of rounds to be played to be customized by the user.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kunal654/rock-paper-scissors-game.git
   cd rock-paper-scissors-game
   ```

2. No additional dependencies are required. You're ready to play!

## Usage

1. Run the script:
   ```bash
   python rock_paper_scissors.py
   ```

2. Follow the prompts to enter the number of rounds to play and the choices for each player.

## Script Overview

### `get_winner(player1_choice, player2_choice)`

Determines the winner of each round based on the choices made by both players.

### `get_choice(player_name)`

Prompts a player to enter their choice (rock, paper, scissors) and validates the input.

### `play_round()`

Manages the gameplay for a single round, including getting choices from both players and determining the winner.

### `rock_paper_scissors_game()`

Orchestrates the entire game, including setting up the number of rounds, playing multiple rounds, and declaring the winner.

## Customization

You can customize the number of rounds to be played by modifying the `rounds` variable in the `rock_paper_scissors_game()` function.

## Contributing

Contributions are welcome! If you have any ideas for improvement or would like to report a bug, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact the repository owner at kunalgautam489@gmail.com.

