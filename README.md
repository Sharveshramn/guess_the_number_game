# guess_the_number_game
🎯 A fun and simple number guessing game in Python! Users try to guess a randomly generated number within a limited number of chances, calculated using binary search logic. Includes friendly prompts and a last-chance warning! --made by Sharveshram

 🎲 Number Guessing Game in Python

A beginner-friendly Python terminal game where the player tries to guess a randomly generated number within a limited number of chances. The number of chances is based on the binary search principle using `log2(range)` for an optimal challenge.

## 🚀 How It Works

1. The player is prompted to start or wait.
2. They enter the upper and lower bounds of the number range.
3. The game randomly picks a number in that range.
4. The player has limited chances to guess the number, calculated using `math.log2(range)`.
5. After each guess, hints are provided.
6. A warning is shown before the last chance.
7. Victory or defeat messages are displayed accordingly.

## 💻 Technologies Used

- Python 3
- `random` module
- `math` module

  ## 🧠 Concepts Practiced

- Conditional statements
- Loops
- User input handling
- Random number generation
- Logarithmic math for optimal guessing

## ✅ To Run the Program
```bash
python guessing_game.py
