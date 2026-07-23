# CodeAlpha 

This repository contains two Python programming tasks completed for Code Alpha. These projects demonstrate fundamental Python concepts, including control flow, data structures, and basic console input/output operations.

## 🎮 Task 1: Hangman Game

A simple, text-based implementation of the classic Hangman game. The player attempts to guess a secret word one letter at a time within a limited number of incorrect guesses.

### Features
* Randomly selects a secret word from a predefined list of 5 words.
* Strict limit of 6 incorrect guesses before game over.
* Validates user input to ensure only single alphabetical characters are accepted.
* Displays the current state of the guessed word and tracks previously guessed letters.

### Key Concepts Used
* `random` module
* `while` loops and `if-else` conditionals
* String manipulation
* Lists

### How to Run
Navigate to the directory containing the file and run the following command in your terminal:
`hangman_game.py`
-----
## 📈 Task 2: Stock Portfolio Tracker

A straightforward console application that calculates the total investment value of a stock portfolio based on manually defined stock prices and user-inputted quantities.

### Features
* Utilizes a hardcoded dictionary of stock prices (e.g., AAPL, TSLA, MSFT).
* Allows users to dynamically enter the stock ticker and the quantity of shares they own.
* Calculates the total value of individual stock holdings and the overall portfolio.
* Includes an option to save the final portfolio summary to a local `.txt` file.

### Key Concepts Used
* Dictionaries
* Standard console Input/Output
* Basic arithmetic operations
* File handling (writing to a `.txt` file)

### How to Run
Navigate to the directory containing the file and run the following command in your terminal:
`stock_portfolio_tracker.py` *(Note: Update the filename if you saved it differently)*

---

## Prerequisites
* **Python 3.x** must be installed on your system to run these scripts. No external libraries or APIs are required.
