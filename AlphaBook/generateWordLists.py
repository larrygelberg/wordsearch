"""
Generate 26 word files (word_A.txt through word_Z.txt) 
containing 15 grade-school appropriate nouns for each letter.
"""

# Dictionary of grade-school nouns by letter
word_lists = {
    'A': ['Apple', 'Animal', 'Ant', 'Arm', 'Art', 'Airplane', 'Alligator', 
          'Astronaut', 'Angel', 'Acorn', 'Ankle', 'Arrow', 'Apron', 'Ambulance', 'Axe'],
    
    'B': ['Ball', 'Book', 'Boy', 'Bear', 'Bed', 'Bike', 'Bird', 'Boat', 
          'Bread', 'Box', 'Bus', 'Butterfly', 'Baby', 'Balloon', 'Bell'],
    
    'C': ['Cat', 'Car', 'Cup', 'Cow', 'Cake', 'Chair', 'Church', 'Coat', 
          'Cookie', 'Cloud', 'Corn', 'Clown', 'Circle', 'Clock', 'Candy'],
    
    'D': ['Dog', 'Door', 'Duck', 'Desk', 'Doll', 'Dress', 'Dinosaur', 'Dish', 
          'Doctor', 'Drum', 'Dragon', 'Deer', 'Diamond', 'Daisy', 'Donkey'],
    
    'E': ['Egg', 'Ear', 'Eye', 'Elephant', 'Earth', 'Elbow', 'Engine', 
          'Eagle', 'Eraser', 'Envelope', 'Exit', 'Explorer', 'Elf', 'Emperor', 'Entrance'],
    
    'F': ['Fish', 'Flower', 'Frog', 'Fox', 'Fire', 'Foot', 'Farm', 'Flag', 
          'Fork', 'Friend', 'Forest', 'Fence', 'Feather', 'Finger', 'Face'],
    
    'G': ['Girl', 'Goat', 'Grass', 'Garden', 'Gate', 'Giraffe', 'Gift', 
          'Grapes', 'Ghost', 'Guitar', 'Glove', 'Gold', 'Gorilla', 'Grocery', 'Grape'],
    
    'H': ['House', 'Horse', 'Hat', 'Hand', 'Heart', 'Hill', 'Hamster', 
          'Hammer', 'Hippo', 'Hair', 'Head', 'Hero', 'Helmet', 'Honey', 'Horn'],
    
    'I': ['Ice', 'Island', 'Insect', 'Igloo', 'Inch', 'Iron', 'Iguana', 
          'Idea', 'Ivy', 'Invitation', 'Infant', 'Inn', 'Instrument', 'Inventor', 'Icicle'],
    
    'J': ['Jar', 'Jacket', 'Juice', 'Jump', 'Jelly', 'Jet', 'Jeep', 'Judge', 
          'Jungle', 'Jaguar', 'Jewel', 'Jeans', 'Journey', 'Joy', 'Juggler'],
    
    'K': ['King', 'Kite', 'Kitten', 'Key', 'Kitchen', 'Koala', 'Knee', 
          'Kangaroo', 'Knight', 'Kettle', 'Keyboard', 'Kidney', 'Ketchup', 'Kid', 'Knot'],
    
    'L': ['Lion', 'Leaf', 'Lamp', 'Leg', 'Lake', 'Lizard', 'Letter', 'Lemon', 
          'Ladder', 'Lunch', 'Library', 'Lobster', 'Lightning', 'Lips', 'Lock'],
    
    'M': ['Moon', 'Mouse', 'Milk', 'Map', 'Money', 'Mountain', 'Monkey', 
          'Monster', 'Mouth', 'Music', 'Mother', 'Mask', 'Mirror', 'Marble', 'Muffin'],
    
    'N': ['Nose', 'Nest', 'Nail', 'Net', 'Night', 'Nurse', 'Neck', 'Nickel', 
          'Notebook', 'Noodle', 'Nut', 'Napkin', 'Number', 'Needle', 'Noise'],
    
    'O': ['Orange', 'Ocean', 'Owl', 'Oven', 'Olive', 'Octopus', 'Onion', 
          'Office', 'Otter', 'Ostrich', 'Oyster', 'Orchestra', 'Oxygen', 'Oar', 'Oak'],
    
    'P': ['Pig', 'Pen', 'Pizza', 'Park', 'Pencil', 'Panda', 'Potato', 'Puppy', 
          'Prince', 'Planet', 'Pickle', 'Piano', 'Pillow', 'Paper', 'Penguin'],
    
    'Q': ['Queen', 'Question', 'Quilt', 'Quarter', 'Quail', 'Quiz', 'Quiet', 
          'Quartz', 'Quest', 'Quicksand', 'Quarry', 'Quartet', 'Quiver', 'Quota', 'Quiche'],
    
    'R': ['Rabbit', 'Rain', 'Robot', 'River', 'Rose', 'Rock', 'Rainbow', 
          'Ring', 'Roof', 'Rocket', 'Ruler', 'Rope', 'Rug', 'Rice', 'Rat'],
    
    'S': ['Sun', 'Star', 'Snake', 'School', 'Shoe', 'Spoon', 'Sheep', 'Snow', 
          'Sock', 'Sister', 'Smile', 'Sandwich', 'Seed', 'Ship', 'Spider'],
    
    'T': ['Tree', 'Table', 'Tiger', 'Train', 'Tooth', 'Turtle', 'Truck', 
          'Teacher', 'Tent', 'Town', 'Treasure', 'Tail', 'Tomato', 'Turkey', 'Toy'],
    
    'U': ['Umbrella', 'Uncle', 'Unicorn', 'Uniform', 'Umpire', 'Ukulele', 
          'Universe', 'Underwear', 'Utensil', 'Urchin', 'Udder', 'Usher', 'Unit', 'Union', 'Upper'],
    
    'V': ['Van', 'Violin', 'Vest', 'Valley', 'Vase', 'Vegetable', 'Village', 
          'Volcano', 'Vulture', 'Vine', 'Vacuum', 'Voice', 'Vote', 'Visitor', 'Vitamin'],
    
    'W': ['Water', 'Window', 'Whale', 'Wheel', 'Wind', 'Wolf', 'Wagon', 
          'Watch', 'Watermelon', 'Winter', 'Wood', 'Worm', 'Wallet', 'Web', 'Wing'],
    
    'X': ['Xylophone', 'Xbox', 'Xerox', 'Xray', 'Xenon', 'Xerus', 'Xenops', 
          'Xebec', 'Xeme', 'Xoanon', 'Xyster', 'Xeric', 'Xiphoid', 'Xyst', 'Xenolith'],
    
    'Y': ['Yard', 'Year', 'Yak', 'Yolk', 'Yogurt', 'Yacht', 'Yam', 'Yarn', 
          'Youth', 'Yell', 'Yo-yo', 'Yellow', 'Yeti', 'Yawn', 'Yield'],
    
    'Z': ['Zebra', 'Zoo', 'Zipper', 'Zone', 'Zero', 'Zucchini', 'Zombie', 
          'Zinnia', 'Zeppelin', 'Zenith', 'Zither', 'Zigzag', 'Zinc', 'Zest', 'Zodiac']
}

def create_word_files():
    """Create 26 directories (A-Z) each containing a word_X.txt file."""
    import os
    
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        # Create directory for the letter
        os.makedirs(letter, exist_ok=True)
        
        # Create word file inside the directory
        filename = os.path.join(letter, f'word_{letter}.txt')
        words = word_lists[letter]
        
        with open(filename, 'w') as f:
            for word in words:
                f.write(word + '\n')
        
        print(f'Created {letter}/word_{letter}.txt with {len(words)} words')

if __name__ == '__main__':
    create_word_files()
    print('\nAll word files created successfully!')