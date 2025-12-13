import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import TextBox, Button, Slider
import numpy as np
import sys

def read_grid(filename):
    """Read grid from file, preserving all characters including spaces."""
    with open(filename, 'r') as f:
        grid = [list(line.rstrip('\n\r')) for line in f if line.strip()]
    return grid

def read_words(filename):
    """Read words from file."""
    with open(filename, 'r') as f:
        words = [line.strip().upper() for line in f if line.strip()]
    return words

def find_word(grid, word):
    """Find all occurrences of word in grid (8 directions)."""
    rows = len(grid)
    cols = len(grid[0])
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
    
    found = []
    
    for row in range(rows):
        for col in range(cols):
            for dy, dx in directions:
                # Check if word fits in this direction
                end_row = row + dy * (len(word) - 1)
                end_col = col + dx * (len(word) - 1)
                
                if 0 <= end_row < rows and 0 <= end_col < cols:
                    # Extract the sequence
                    match = True
                    for i in range(len(word)):
                        y = row + dy * i
                        x = col + dx * i
                        if grid[y][x] != word[i]:
                            match = False
                            break
                    
                    if match:
                        found.append(((row, col), (end_row, end_col)))
    
    return found

def draw_capsule(ax, start, end, cols, rows, h_spacing, v_spacing, font_size):
    """Draw a capsule (rounded rectangle) around found word."""
    y1, x1 = start
    y2, x2 = end
    
    # Convert grid coordinates to plot coordinates with spacing
    px1, py1 = x1 * h_spacing, rows - y1 - 1
    px2, py2 = x2 * h_spacing, rows - y2 - 1
    py1 *= v_spacing
    py2 *= v_spacing
    
    # Calculate center and angle
    center_x = (px1 + px2) / 2
    center_y = (py1 + py2) / 2
    
    dx = px2 - px1
    dy = py2 - py1
    length = np.sqrt(dx**2 + dy**2)
    angle = np.degrees(np.arctan2(dy, dx))
    
    # Capsule dimensions based on font size
    # Height is 110% of font size (1.1x)
    # Font size in matplotlib roughly corresponds to height in data units when spacing is 1.0
    # Scale by 0.05 per font point as a rough approximation
    capsule_height = font_size * 0.06 * max(h_spacing, v_spacing)  # Reduced from 0.055
    width = length + capsule_height
    height = capsule_height
    
    # Adjust y-offset based on whether capsule is angled
    # For horizontal/vertical words, shift down slightly for better visual alignment
    is_angled = abs(dx) > 0.01 and abs(dy) > 0.01  # Check if diagonal
    y_offset = height/1.7 if is_angled else height/2.35

    # Create rounded rectangle (capsule)
    capsule = patches.FancyBboxPatch(
        (center_x - width/2, center_y - y_offset),
        width, height,
        boxstyle=f"round,pad=0.05,rounding_size={height/2}",
        linewidth=1.5,
        edgecolor='black',
        facecolor=(0.7, 0.7, 0.7, 0.3),  # RGBA: gray with alpha only on fill
        transform=ax.transData
    )
    
    # Rotate the capsule
    t = plt.matplotlib.transforms.Affine2D().rotate_deg_around(
        center_x, center_y, angle
    ) + ax.transData
    capsule.set_transform(t)
    
    return capsule

def display_word_search(grid_file, words_file, name):
    """Main function to display word search with found words highlighted."""
    # Read files
    grid = read_grid(grid_file)
    words = read_words(words_file)
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Calculate figure size that fits on screen
    max_height = 9.0
    max_width = 14.0
    
    ideal_width = max(6, cols * 0.6)
    ideal_height = max(5, rows * 0.6) + 2.5  # extra for controls and sliders
    
    fig_width = min(ideal_width, max_width)
    fig_height = min(ideal_height, max_height)
    
    # Create figure
    fig = plt.figure(figsize=(fig_width, fig_height))
    
    # Main grid axes - leave space at bottom for controls
    ax = plt.axes([0.1, 0.35, 0.8, 0.6])
    
    # Find words first
    found_words = []
    word_locations = {}
    for word in words:
        locations = find_word(grid, word)
        if locations:
            found_words.append(word)
            word_locations[word] = locations
    
    # Print results
    print(f"Found {len(found_words)} out of {len(words)} words:")
    for word in found_words:
        print(f"  ✓ {word}")
    
    missing = set(words) - set(found_words)
    if missing:
        print(f"\nNot found:")
        for word in missing:
            print(f"  ✗ {word}")
    
    # Storage for drawn elements
    letter_texts = []
    capsule_patches = []
    
    # Initial spacing and size values
    h_spacing = [1.0]
    v_spacing = [1.0]
    letter_size = [14]
    
    def redraw():
        """Redraw the grid with current spacing and size."""
        ax.clear()
        letter_texts.clear()
        capsule_patches.clear()
        
        # Display grid letters
        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                if letter != ' ':
                    txt = ax.text(j * h_spacing[0], (rows - i - 1) * v_spacing[0], letter, 
                           ha='center', va='center', 
                           fontsize=letter_size[0], fontfamily='monospace')
                    letter_texts.append(txt)
        
        # Draw capsules for found words
        for word in found_words:
            for start, end in word_locations[word]:
                capsule = draw_capsule(ax, start, end, cols, rows, h_spacing[0], v_spacing[0], letter_size[0])
                ax.add_patch(capsule)
                capsule_patches.append(capsule)
        
        # Set up plot with adjusted limits - add extra padding for capsules
        padding = 0.8  # Extra padding to prevent capsule clipping
        ax.set_xlim(-padding * h_spacing[0], (cols - 1 + padding) * h_spacing[0])
        ax.set_ylim(-padding * v_spacing[0], (rows - 1 + padding) * v_spacing[0])
        ax.set_aspect('equal')
        ax.axis('off')
        fig.canvas.draw_idle()
    
    # Initial draw
    redraw()
    
    # Create sliders
    ax_h_slider = plt.axes([0.14, 0.24, 0.7, 0.03])
    h_slider = Slider(ax_h_slider, 'H-Spacing', 0.5, 2.0, valinit=1.0, valstep=0.05)
    
    ax_v_slider = plt.axes([0.14, 0.19, 0.7, 0.03])
    v_slider = Slider(ax_v_slider, 'V-Spacing', 0.5, 2.0, valinit=1.0, valstep=0.05)
    
    ax_size_slider = plt.axes([0.14, 0.14, 0.7, 0.03])
    size_slider = Slider(ax_size_slider, 'Letter Size', 10, 40, valinit=14, valstep=1)
    
    def update_h_spacing(val):
        h_spacing[0] = val
        redraw()
    
    def update_v_spacing(val):
        v_spacing[0] = val
        redraw()
    
    def update_letter_size(val):
        letter_size[0] = val
        redraw()
    
    h_slider.on_changed(update_h_spacing)
    v_slider.on_changed(update_v_spacing)
    size_slider.on_changed(update_letter_size)
    
    # Create filename textbox
    default_filename = f'solution_{name}.png'
    ax_textbox = plt.axes([0.15, 0.06, 0.5, 0.05])
    textbox = TextBox(ax_textbox, 'Filename: ', initial=default_filename)
    textbox.label.set_size(10)
    
    # Create save button
    ax_button = plt.axes([0.7, 0.06, 0.15, 0.05])
    button = Button(ax_button, 'Download', color='lightblue', hovercolor='skyblue')
    
    # Store filename
    filename_container = {'name': default_filename}
    
    def update_filename(text):
        filename_container['name'] = text
    
    def save_figure(event):
        filename = filename_container['name']
        if not filename:
            filename = default_filename
        
        # Save only the main axes (grid), not the controls
        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig(filename, bbox_inches=extent.expanded(1.2, 1.2), dpi=300)
        print(f"\nSaved to: {filename}")
    
    textbox.on_submit(update_filename)
    textbox.on_text_change(update_filename)
    button.on_clicked(save_figure)
    
    # Try to position window
    manager = plt.get_current_fig_manager()
    try:
        manager.window.wm_geometry("+0+0")
    except:
        pass
    
    plt.show()

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordsearch.py <name>")
        print("\nExample: python wordsearch.py puzzle1")
        print("\n  This will look for:")
        print("    - grid_<name>.txt (e.g., grid_puzzle1.txt)")
        print("    - words_<name>.txt (e.g., words_puzzle1.txt)")
        sys.exit(1)
    
    name = sys.argv[1]
    grid_file = f"grid_{name}.txt"
    words_file = f"words_{name}.txt"
    
    print(f"Loading grid from: {grid_file}")
    print(f"Loading words from: {words_file}\n")
    
    try:
        display_word_search(grid_file, words_file, name)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)