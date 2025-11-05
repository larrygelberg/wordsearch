import sys
import string
import random
import argparse
import copy
from collections import Counter

# Function to print a list of words in four columns
def pretty_print(mylist):
    extras = 4 - len(mylist)%4
    if extras >= 4:
        extras = 0
    for i in range (0,extras):
        mylist.append("")
    print('\n'.join("%-16s %-16s %-16s %s" % (mylist[i], mylist[i + len(mylist) // 4], mylist[i + len(mylist) * 2 // 4], mylist[i + len(mylist) * 3 // 4]) for i in range(len(mylist) // 4)))

# Function to fill in 'empty' spaces with '.' for debugging
def debug_fill():
    for i in range(height):
        for j in range(width):
            if (final_game[j][i] == 0):
                final_game[j][i] = '.'

# Function to fill in 'empty' spaces with random characters
def simple_fill():
    for i in range(height):
        for j in range(width):
            if (final_game[j][i] ==  '.'):
                final_game[j][i] = ' '
            elif (final_game[j][i] == 0):
                final_game[j][i] = random.choice(string.ascii_uppercase)

# Function to fill in 'empty' spaces with sneaky characters based on prevalence of letters in the word set
def hairy_fill():
    # First, build a histogram of frequency of letters in the word set
    all_characters = ''.join(words)
    character_count = Counter(all_characters)
    most_common = character_count.most_common(7)
    most_frequent_chars = [char for char, count in most_common]
    if debug:
        print (most_frequent_chars)

    # fill in the empty spaces based on the most frequent letters
    for i in range(height):
        for j in range(width):
            if (final_game[j][i] ==  '.'):
                final_game[j][i] = ' '
            elif (final_game[j][i] == 0):
                final_game[j][i] = random.choice(most_frequent_chars)

# Function to print the game board
def print_game():
    endchar = '' if nospace else ' '
    for i in range(height):
        print ('')
        for j in range(width):
            print(str(final_game[j][i]),end=endchar)

def print_shape():
    print(shape,width,height)
    for i in range(height):
        print ('')
        for j in range(width):
            print(str(shape[j][i]),end=' ')    

# Function to read the words from a file
def read_words(fname):
    result = []
    with open(fname) as f:
        content = f.readlines()
    # turn the words into uppercase and remove any newline characters
    for word in content:
        if (word != "\n"):
            result.append(word.replace('\n', '').upper())
    # sort the list from longest to shortest
    return sorted(result, key=len, reverse=True)

# Function to see if the proposed character's space is available
def check_char(x, y, char):
    if x < 0 or x >= width or y<0 or y >= height:
        return False
    bar = game[x][y]
    return game[x][y] == 0 or game[x][y] == char

# Function to insert a word into the game board
#    direction is a value 0-8 indicating if the word should go in horizontally, vertically, or diagonally
#    and forward or backward
#    This function tries to place the word 'attempt_limit' times before it gives up
def insert(word, direction):
    attempt_limit = 2000     # adjust this to try more (or less) times
    for attempt in range (0, attempt_limit):
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)

        forward = True if direction & 1 else False
        horizontal = True if direction & 2  else False
        diagonal = True if direction & 4 else False
        #if debug:
        #    print(attempt, ": Trying", word,"at",x, y)

        if diagonal:
            # Horizontal and Vertical words
            if horizontal:
                # Horizontal
                if x+len(word) <= width and y+len(word) <= height:
                    safe = True
                    for i in range(0, len(word)):
                        if forward:
                            safe = check_char(x+i, y+i, word[i])
                        else:
                            safe = check_char(x+len(word)-i-1, y+i, word[i])
                        if not safe:
                            break
                    if safe:
                        for i in range(0, len(word)):
                            if forward:
                                game[x+i][y+i] = word[i]
                            else:
                                game[x+len(word)-i-1][y+i] = word[i]
                        break
            else:
                # Vertical
                if x+len(word) <= width and y+len(word) <= height:
                    safe = True
                    for i in range(0, len(word)):
                        if forward:
                            safe = check_char(x+len(word)-i-1, y+i, word[i])
                        else:
                            safe = check_char(x+len(word)-i-1, y+len(word)-i-1, word[i])
                        if not safe:
                            break
                    if safe:
                        for i in range(0, len(word)):
                            if forward:
                                game[x+len(word)-i-1][y+i] = word[i]
                            else:
                                game[x+len(word)-i-1][y+len(word)-i-1] = word[i]
                        break            
        else:
            # Horizontal and Vertical words
            if horizontal:
                # Horizontal
                if x+len(word) <= width:
                    safe = True
                    for i in range(0, len(word)):
                        if forward:
                            safe = check_char(x+i, y, word[i])
                        else:
                            safe = check_char(x+len(word)-i-1, y, word[i])
                        if not safe:
                            break
                    if safe:
                        for i in range(0, len(word)):
                            if forward:
                                game[x+i][y] = word[i]
                            else:
                                game[x+len(word)-i-1][y] = word[i]
                        break
            else:
                # Vertical
                if y+len(word) <= height:
                    safe = True
                    for i in range(0, len(word)):
                        if forward:
                            safe = check_char(x, y+i, word[i])
                        else:
                            safe = check_char(x, y+len(word)-i-1, word[i])
                        if not safe:
                            break
                    if safe:
                        for i in range(0, len(word)):
                            if forward:
                                game[x][y+i] = word[i]
                            else:
                                game[x][y+len(word)-i-1] = word[i]
                        break
                        
    if attempt < attempt_limit-1:
        used.append(word)
    else:
        unused.append(word)

################################################################

final_game = []
final_unused = []
final_used = []
game = []
shape = []

# Create the parser
parser = argparse.ArgumentParser(description='Process some files and options.')

# Required argument
parser.add_argument('words_file', type=str, help='The words file')

# Optional arguments
parser.add_argument('--width', type=int, help='Optional width')
parser.add_argument('--height', type=int, help='Optional height')
parser.add_argument('--hard', action='store_true', help='Optional hard flag')
parser.add_argument('--shape_file', type=str, help='Optional shape file')
parser.add_argument('--no_space', action='store_true', help='Do not put spaces in game output')
parser.add_argument('--debug', action='store_true', help='Debug Flag')

# Parse the arguments
args = parser.parse_args()

# Access the arguments
width = 10 if args.width is None else args.width
height = 10 if args.height is None else args.height
easy = False if args.hard else True
debug = True if args.debug else False
nospace = True if args.no_space else False

if args.shape_file is not None:
    try:
        with open(args.shape_file, 'r') as file:
            tempShape = []
            height = 0
            for line in file:
                width = len(line)
                for c in line:
                    if c == '0':
                        c = 0
                    if c != '\n':
                        tempShape.append(c)
                height = height + 1

            shape = [[tempShape[i*width + j] for i in range(height)] for j in range(width)]

            if debug:
                print_shape()

    except FileNotFoundError:
        print(f"Error: The file '{args.shape_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# read the word file
words = read_words(args.words_file)
if debug:
    print(words)

# loop over placements trying to find the most optimal board
game_attempt_limit = 1000
min_placed_words = len(words)
for g in range(0,game_attempt_limit):
    unused = []
    used = []
    # initialize the game board
    if shape:
        game = copy.deepcopy(shape)
    else:    
        game = [[0 for i in range(height)] for j in range(width)]

    # stick words into the game board
    for word in words:
        direction = random.randint(0,7)
        insert(word, direction)

    placed_words = len(unused)
    if debug:
        print("Board",g,"has",placed_words,"words left.")

    if placed_words == 0:
        final_game = game
        final_unused = unused
        final_used = used
        break

    if placed_words < min_placed_words:
        final_game = game
        final_unused = unused
        final_used = used
        min_placed_words = placed_words

# fill in remaining spaces with random letters
if debug:
    debug_fill()
elif easy:
    simple_fill()
else:
    hairy_fill()

# print the results
print_game()

print()
print()
print("Find these words: ")
pretty_print(sorted(final_used))

# print any words that couldn't be placed
if len(unused) > 0:
    print()
    print("Unused:",final_unused)
    print()



