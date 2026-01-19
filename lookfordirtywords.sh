#!/bin/zsh

# Check if dirty_words.txt exists in current directory
if [[ ! -f "dirty_words.txt" ]]; then
    echo "Error: dirty_words.txt not found in current directory"
    exit 1
fi

# Check if word_search.py exists
if [[ ! -f "../testgrid.py" ]]; then
    echo "Error: ../testgrid.py not found in current directory"
    exit 1
fi

# List of directories to check
directories=(
    "Alabama"
"Idaho"
"Missouri"
"Pennsylvania"
"Washington"
"Alaska"
"Illinois"
"Montana"
"PuertoRico"
"WestVirginia"
"Arizona"
"Indiana"
"Nebraska"
"RhodeIsland"
"Wisconsin"
"Arkansas"
"Iowa"
"Nevada"
"SouthCarolina"
"Wyoming"
"Kansas"
"NewHampshire"
"SouthDakota"
"California"
"Kentucky"
"NewJersey"
"Tennessee"
"Colorado"
"Louisiana"
"NewMexico"
"Texas"
"Connecticut"
"Maine"
"NewYork"
"DC"
"Maryland"
"NorthCarolina"
"Delaware"
"Massachusetts"
"NorthDakota"
"Florida"
"Michigan"
"Ohio"
"Utah"
"Georgia"
"Minnesota"
"Oklahoma"
"Vermon"
"Hawaii"
"Mississippi"
"Oregon"
"Virginia"
    # Add more directories here
)

# Get the absolute path to dirty_words.txt
dirty_words_file="$(pwd)/dirty_words.txt"

echo "Starting word search across directories..."
echo "Using word list: $dirty_words_file"
echo "=" * 60

# Loop through each directory
for dir in "${directories[@]}"; do
    if [[ ! -d "$dir" ]]; then
        echo "\nWarning: Directory '$dir' does not exist, skipping..."
        continue
    fi
    
    echo "\n\nChecking directory: $dir"
    echo "-" * 60
    
    # Find all grid* files in the directory
    grid_files=("$dir"/grid*)
    
    if [[ ${#grid_files[@]} -eq 0 ]] || [[ ! -e "${grid_files[1]}" ]]; then
        echo "No grid files found in $dir"
        continue
    fi
    
    # Process each grid file
    for grid_file in "${grid_files[@]}"; do
        if [[ -f "$grid_file" ]]; then
            echo "\n  Processing: $(basename $grid_file)"
            python3 ../testgrid.py "$grid_file" "$dirty_words_file"
        fi
    done
done

echo "\n\nWord search complete!"