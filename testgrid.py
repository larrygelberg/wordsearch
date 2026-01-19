import sys

def read_grid(filename):
    """Read the grid file and return a 2D list of characters."""
    with open(filename, 'r') as f:
        grid = []
        for line in f:
            line = line.rstrip('\n\r')  # Remove only newline characters
            if line:
                # Convert each character to uppercase, including spaces
                row = [char.upper() for char in line]
                grid.append(row)
    
    # Validate grid is not empty
    if not grid:
        raise ValueError("Grid file is empty")
    
    # Check that all rows have the same length
    row_lengths = [len(row) for row in grid]
    if len(set(row_lengths)) > 1:
        raise ValueError(f"Grid rows have inconsistent lengths: {row_lengths}")
    
    return grid

def read_words(filename):
    """Read the word file and return a list of words."""
    with open(filename, 'r') as f:
        words = [line.strip().upper() for line in f if line.strip()]
    return words

def search_direction(grid, word, row, col, dr, dc):
    """
    Search for a word starting at (row, col) in direction (dr, dc).
    dr and dc represent the row and column deltas for each step.
    Returns True if word is found, False otherwise.
    """
    if not grid or not grid[0]:
        return False
    
    rows, cols = len(grid), len(grid[0])
    
    for i in range(len(word)):
        r, c = row + i * dr, col + i * dc
        
        # Check bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        
        # Additional safety check for row length
        if c >= len(grid[r]):
            return False
        
        # Check character match
        if grid[r][c].upper() != word[i]:
            return False
    
    return True

def find_word(grid, word):
    """
    Search for a word in the grid in all 8 directions.
    Returns the position and direction if found, None otherwise.
    """
    if not grid or not grid[0] or not word:
        return None
    
    rows, cols = len(grid), len(grid[0])
    
    # 8 directions: right, left, down, up, and 4 diagonals
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    for row in range(rows):
        for col in range(min(cols, len(grid[row]))):
            for dr, dc in directions:
                if search_direction(grid, word, row, col, dr, dc):
                    return (row, col, dr, dc)
    
    return None

def solve_word_search(grid_file, word_file):
    """Main function to solve the word search puzzle."""
    grid = read_grid(grid_file)
    words = read_words(word_file)
    
    found = []
    not_found = []
    
    for word in words:
        result = find_word(grid, word)
        if result:
            found.append(word)
        else:
            not_found.append(word)
    
    return found, not_found

def main():
    if len(sys.argv) != 3:
        print("Usage: python word_search.py <grid_file> <word_file>")
        sys.exit(1)
    
    grid_file = sys.argv[1]
    word_file = sys.argv[2]
    
    try:
        found, not_found = solve_word_search(grid_file, word_file)
        
        print("WORDS FOUND:")
        print("=" * 40)
        for word in found:
            print(f"  {word}")
        print(f"\nTotal found: {len(found)}")
        
        print("\n" + "=" * 40)
        print("WORDS NOT FOUND:")
        print("=" * 40)
        for word in not_found:
            print(f"  {word}")
        print(f"\nTotal not found: {len(not_found)}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()