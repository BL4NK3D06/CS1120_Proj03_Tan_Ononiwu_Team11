# Project No: 3
# Author: Justin Tan
# Description: Boggle game board class with recursion, palindrome check, and word validation.

# Import the modules that will be used
import random
import string

# Design the class that contains the display, is_palindrome, and find_path function
class BoggleBoard:

    # Define the initializer function.
    def __init__(self, seed=None):
        # Set the seed to a random seed if the user does not input a seed.
        if seed is not None:
            random.seed(seed)
        # Using the random and string module imported, design a 4x4 box using a two dimension list.
        self.board = [[random.choice(string.ascii_uppercase) for _ in range(4)] for _ in range(4)]


    # The display function would display the board according to the format, with the highlight or not.
    def display(self, highlight=None):

        # Create a for loop that displays the borders of each grid
        for row in range(4):
            print("+---+ " * 4)
            # Set up an accumulator that will be used to print each row
            row_str = ""
            for col in range(4):
                ch = self.board[row][col]
                # If there is a list used as the argument for this method, it will highlight the path, or else display it normally.
                if highlight and (row, col) in highlight:
                    row_str += f"|<{ch}>| "
                else:
                    row_str += f"| {ch} | "
        # Display each row
            print(row_str.strip())
        print("+---+ " * 4)

    # This function checks whether the word entered by the user is a palindrome or not and return TRUE/FALSE
    def is_palindrome(self, word):
        # Define the base case of the recursive function that returns True
        if len(word) <= 1:
            return True
        # If the first and last character is different, return False
        if word[0] != word[-1]:
            return False
        # Or else, let the recursive function check the next index from both sides.
        return self.is_palindrome(word[1:-1])


    # This function finds the path of the word entered by the user and validate whether the word is on the board.
    def find_path(self, word):

        # Define a recursive function to search for whether the next letter is the neighbor of the first letter.
        def search(r, c, index, visited, path):

            # This is the base case, where the function stops if the index which starts from 0 reaches the length of the word.
            if index == len(word):
                return True
            # If the coordinate given is out of the 4x4 grid, this path is a failure and returns False.
            if not (0 <= r < 4 and 0 <= c < 4):
                return False
            # If the coordinates given have been visited before, this path is also a failure and returns False.
            if (r, c) in visited:
                return False
            # If the letter on the coordinate of the board is not letter on the index of the word, return False.
            if self.board[r][c] != word[index]:
                return False

            # If it passes all those requirements, add the coordinate to the list of visited.
            visited.add((r, c))
            # Also, append the coordinate to a list named path.
            path.append((r, c))

            # The neighbours for the current coordinates is defined below
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            # Using a for loop, check whether any of the neighbors fulfill the requirements
            # and continue the loop until it reaches the base case or hit any restrictions.
            for nr, nc in neighbors:
                if search(nr, nc, index + 1, visited, path):
                    return True

            # If the current path fail, remove the coordinates from the visited set
            visited.remove((r, c))
            # Also, pop the elements in the list
            path.pop()
            # Then return False
            return False

        # Now, set the for loop to check whether the word, and it's path is on the board.
        for row in range(4):
            for col in range(4):
                # Set an empty list
                path = []
                # If the function returns True, which signals the function reaching the base case
                # and also means that this path is the right path thus returning the correct path as a list.
                if search(row, col, 0, set(), path):
                    return path
        # Return an empty list if all paths fails
        return []

        # This function returns a filled or empty list, which also serves as a True or False in the main
        # function because Python determines that empty lists are falsy in Boolean context and vice versa.