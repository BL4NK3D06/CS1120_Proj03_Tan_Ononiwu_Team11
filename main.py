# Project No: 3
# Author: Justin Tan
# Description: The main function that class the BoggleBoard class and executes the program

# Import the Boggle Board class
from Boggle_board import BoggleBoard

# Design the main function to run the program
def main():

    # Ask for input of the seed
    seed = int(input("Enter seed: "))

    # Declare an instance of the BoggleBoard
    board = BoggleBoard(seed)
    # Display the board using the existing method in the class
    board.display()

    # Ask the user for a word in the board
    word = input("Enter word (in UPPERcase): ").strip().upper()

    # Display whether the word is found in the board using the find_path method in the class.
    if board.find_path(word):
        print("Nice Job!")
    else:
        print("I don't see that word.")

    # Check whether the word is a palindrome using the method is_palindrome and tell the user.
    if board.is_palindrome(word):
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")

    # Using the find_path method again, display the highlighted board if the word is found or warn the user if it's not found.
    if board.find_path(word):
        path = board.find_path(word)
        board.display(highlight=set(path))
    else:
        print("Are we looking at the same board?")


# Start the function
if __name__ == "__main__":
    main()