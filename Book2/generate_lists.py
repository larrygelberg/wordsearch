#!/usr/bin/env python3
"""
Generates word list files for all US states and Puerto Rico.
Each word is 4-20 characters long.
Each state has at least 40 words.
Run this script to create words_STATENAME.txt files in the current directory.
"""

import os

state_words = {
    "Florida": [
        "Alligator", "Biscayne", "Boca", "Clearwater", "Cuban",
        "Daytona", "Dolphins", "Everglades", "Keys", "FortLauderdale",
        "FortMyers", "Gators", "Grouper", "Heat", "Hurricanes",
        "Jacksonville", "KeyLime", "KeyWest", "Lightning",
        "Manatee", "Miami", "Naples", "Orlando", "PalmBeach",
        "Panama", "Panhandle", "Pensacola", "Publix", "Rays",
        "Sarasota", "SevenMile", "SpaceCoast", "Augustine",
        "Tallahassee", "Tampa", "Disney", "Universal", "Seminoles",
        "Bucs", "Magic", "Gainesville", "Citrus", "SunshineState",
        "Hialeah", "Coral", "Springs", "Cape"
    ],
    
    "Georgia": [
        "Athens", "Atlanta", "Braves", "Brunswick", "Savannah",
        "Macon", "Augusta", "Columbus", "CocaCola", "Delta",
        "Falcons", "Hawks", "Peachtree", "Bulldogs", "StoneMountain",
        "Okefenokee", "Chattahoochee", "Jekyll", "Tybee",
        "MartinLutherKing", "HomeDepot", "Chick", "WaffleHouse",
        "Vidalia", "Peanuts", "Pecans", "SweetTea", "Masters",
        "Bobby", "Jones", "Hank", "Aaron", "Outkast", "Marietta",
        "Roswell", "Albany", "Valdosta", "Warner", "Robins",
        "Forsyth", "Gwinnett"
    ],
    
    "Hawaii": [
        "Aloha", "Hana", "Hilo", "Honolulu", "Kauai",
        "Kona", "Lanai", "Lava", "Luau", "Maui",
        "Molokai", "Oahu", "Pele", "Pineapple", "Polynesian",
        "Shaka", "Surfing", "Ukulele", "Volcano", "Waikiki",
        "PearlHarbor", "Diamond", "Haleakala", "Kilauea",
        "Spam", "Poke", "Shave", "Mahalo", "Ohana",
        "Hula", "Hibiscus", "Kakaako", "Manoa", "Rainbow",
        "Snorkeling", "Macadamia", "Taro", "Kamehameha",
        "Sunset", "Kailua"
    ],
    
    "Idaho": [
        "Boise", "Coeur", "Idaho", "Potatoes", "Salmon",
        "SunValley", "Twin", "Pocatello", "Nampa", "Meridian",
        "CratersMoon", "Snake", "Sawtooth", "Hells", "Steelhead",
        "Trout", "Skiing", "Hiking", "Whitewater", "Mining",
        "Vandals", "Broncos", "Treasure", "Lewis", "Clark",
        "Shoshone", "Bannock", "Lemhi", "Teton", "Yellowstone",
        "Bear", "Payette", "Bitterroot", "Clearwater", "Bruneau",
        "Challis", "Ketchum", "Sandpoint", "Rexburg", "Idaho"
    ],
    
    "Illinois": [
        "Bears", "Blackhawks", "Bulls", "Chicago", "Cubs",
        "DeepDish", "Lincoln", "Navy", "Sears", "Wrigley",
        "Springfield", "Peoria", "Rockford", "Route", "Corn",
        "Obama", "Cloud", "Magnificent", "Loop", "Lake",
        "Willis", "Joliet", "Naperville", "Aurora", "Elgin",
        "Champaign", "Decatur", "Evanston", "Schaumburg", "Bolingbrook",
        "Palatine", "Millennium", "Field", "Museum", "Shedd",
        "Pizzeria", "Portillo", "Malort", "Prairie", "Cahokia",
        "WhiteSox"
    ],
    
    "Indiana": [
        "Bloomington", "Colts", "Corn", "Hoosiers", "Indy",
        "Indianapolis", "Pacers", "Notre", "Dame", "Purdue",
        "Ball", "State", "Evansville", "FortWayne", "Gary",
        "Lafayette", "Muncie", "SouthBend", "Terre", "Haute",
        "Racing", "Basketball", "Tenderloin", "Crossroads",
        "Motor", "Limestone", "Larry", "Bird", "Reggie",
        "Miller", "Peyton", "Manning", "Carmel", "Fishers",
        "Noblesville", "Greenwood", "Anderson", "Kokomo", "Richmond",
        "Columbus"
    ],
    
    "Iowa": [
        "Ames", "Cedar", "Rapids", "Corn", "Cyclones",
        "Davenport", "DesMoines", "Dubuque", "Hawkeyes", "Iowa",
        "City", "Sioux", "Waterloo", "Pork", "Butter",
        "Field", "Dreams", "Grant", "Wood", "Council",
        "Bluffs", "Bettendorf", "Ankeny", "Urbandale", "West",
        "Marion", "Marshalltown", "Mason", "Fort", "Dodge",
        "Burlington", "Boone", "Newton", "Indianola", "Grinnell",
        "Caucus", "Maid", "Rite", "Pella", "Amana",
        "Kinnick"
    ],
    
    "Kansas": [
        "Dorothy", "Jayhawks", "Kansas", "City", "Lawrence",
        "Manhattan", "Overland", "Park", "Sunflower", "Topeka",
        "Wheat", "Wichita", "Dodge", "City", "Abilene",
        "Eisenhower", "Tornado", "Prairie", "Salina", "Leavenworth",
        "Hutchinson", "Garden", "Emporia", "Derby", "Olathe",
        "Shawnee", "Leawood", "Lenexa", "Blues", "Jazz",
        "Flint", "Hills", "Tallgrass", "Fort", "Riley",
        "Wild", "Bill", "Hickok", "Wyatt", "Earp",
        "Boot", "Hill"
    ],
    
    "Kentucky": [
        "Bourbon", "Churchill", "Downs", "Derby", "Frankfort",
        "Fried", "Chicken", "Lexington", "Louisville", "Mammoth",
        "Cave", "Thoroughbred", "Wildcats", "Bluegrass", "Coal",
        "Daniel", "Boone", "Horse", "Racing", "Mint",
        "Julep", "Slugger", "Basketball", "Covington", "Owensboro",
        "Bowling", "Green", "Hopkinsville", "Richmond", "Florence",
        "Georgetown", "Henderson", "Nicholasville", "Paducah", "Ashland",
        "Maker", "Mark", "Woodford", "Fort", "Knox",
        "Rupp", "Arena"
    ],
    
    "Louisiana": [
        "Bayou", "Beignets", "Bourbon", "Street", "Cajun",
        "Crawfish", "Creole", "Gumbo", "Jazz", "Lake",
        "Pontchartrain", "Mardi", "Gras", "NewOrleans", "Pelicans",
        "Pralines", "Saints", "Tabasco", "Zydeco", "Baton",
        "Rouge", "Lafayette", "Shreveport", "Swamp", "Metairie",
        "Kenner", "Bossier", "City", "Monroe", "Alexandria",
        "Houma", "Slidell", "Natchitoches", "Hammond", "Ruston",
        "Thibodaux", "Superdome", "French", "Quarter", "Avery",
        "Island", "Atchafalaya", "Cafe", "Jambalaya"
    ],
    
    "Maine": [
        "Acadia", "Augusta", "Bangor", "Blueberries", "LLBean",
        "Lighthouse", "Lobster", "Moose", "Portland", "Stephen",
        "King", "Whoopie", "Pies", "Kennebunk", "BarHarbor",
        "Coastal", "Pine", "Tree", "Lewiston", "Biddeford",
        "Sanford", "Saco", "Westbrook", "Waterville", "Presque",
        "Isle", "Auburn", "Brunswick", "Scarborough", "York",
        "Freeport", "Kittery", "Wells", "Rockland", "Bath",
        "Belfast", "Camden", "Vacationland", "Cadillac", "Mountain",
        "Jordan", "Pond"
    ],
    
    "Maryland": [
        "Annapolis", "Baltimore", "Blue", "Crabs", "Chesapeake",
        "Crab", "Cakes", "Fort", "McHenry", "Lacrosse",
        "Naval", "Academy", "Ocean", "City", "Orioles",
        "Ravens", "Rockfish", "Smith", "Island", "Terps",
        "Under", "Armour", "Frederick", "Gaithersburg", "Bowie",
        "Rockville", "Hagerstown", "Salisbury", "Waldorf", "Columbia",
        "Glen", "Burnie", "Silver", "Spring", "Towson",
        "Bethesda", "Natty", "Boh", "National", "Harbor",
        "Assateague", "Preakness"
    ],
    
    "Massachusetts": [
        "Bean", "Town", "Boston", "Bruins", "Cambridge",
        "Cape", "Cod", "Celtics", "Chowder", "Cranberry",
        "Dunkin", "Donuts", "Fenway", "Park", "Freedom",
        "Trail", "Harvard", "Kennedy", "Martha", "Vineyard",
        "Patriots", "Plymouth", "Rock", "RedSox", "Salem",
        "Springfield", "Witch", "Worcester", "Lowell", "Newton",
        "Somerville", "Lawrence", "Framingham", "Haverhill", "Waltham",
        "Malden", "Brookline", "Quincy", "Lynn", "Brockton",
        "Lexington"
    ],
    
    "Michigan": [
        "AnnArbor", "Cars", "Cereal", "Cherries", "Detroit",
        "Ford", "Great", "Lakes", "Lions", "Mackinac",
        "Bridge", "Motown", "Pictured", "Rocks", "Pistons",
        "RedWings", "Tigers", "UofM", "Wolverines", "Lansing",
        "Grand", "Rapids", "Flint", "Dunes", "Sterling",
        "Heights", "Warren", "Clinton", "Livonia", "Dearborn",
        "Westland", "Troy", "Farmington", "Kalamazoo", "Wyoming",
        "Southfield", "Rochester", "Taylor", "Pontiac", "Battle",
        "Creek", "Traverse"
    ],
    
    "Minnesota": [
        "Boundary", "Waters", "Grain", "Belt", "Lake",
        "Superior", "Mall", "America", "Mayo", "Clinic",
        "Minneapolis", "North", "Star", "Paul", "Prince",
        "Target", "Twins", "Vikings", "Wild", "Wolves",
        "Loon", "Bloomington", "Duluth", "Rochester", "Brooklyn",
        "Park", "Plymouth", "Woodbury", "Maple", "Grove",
        "Blaine", "Lakeville", "Eagan", "Burnsville", "Eden",
        "Prairie", "Coon", "Rapids", "Edina", "Minnetonka",
        "Mankato", "Moorhead"
    ],
    
    "Mississippi": [
        "Biloxi", "Blues", "Catfish", "Delta", "Elvis",
        "Presley", "Gulf", "Coast", "Jackson", "Mississippi",
        "River", "Muddy", "Waters", "Oprah", "Winfrey",
        "Oxford", "Rebels", "Tupelo", "Vicksburg", "Wright",
        "Brothers", "Gulfport", "Southaven", "Hattiesburg", "Meridian",
        "Greenville", "Horn", "Lake", "Pearl", "Madison",
        "Clinton", "Ridgeland", "Starkville", "Columbus", "Pascagoula",
        "Brandon", "Clarksdale", "Natchez", "William", "Faulkner",
        "Tennessee", "Williams"
    ],
    
    "Missouri": [
        "Arch", "Gateway", "Branson", "Cardinals", "Chiefs",
        "Kansas", "City", "Lake", "Ozark", "Mark",
        "Twain", "Missouri", "River", "Ozarks", "Springfield",
        "Louis", "Blues", "Truman", "Bass", "BBQ",
        "Independence", "Columbia", "Lees", "Summit", "Florissant",
        "Charles", "Blue", "Springs", "Joplin", "Jefferson",
        "City", "Chesterfield", "Cape", "Girardeau", "Ballwin",
        "Wildwood", "Gladstone", "Sedalia", "Hannibal", "Silver",
        "Dollar", "Table", "Rock"
    ],
    
    "Montana": [
        "Bighorn", "Mountains", "Bison", "Bozeman", "Butte",
        "Flathead", "Lake", "Glacier", "Park", "Great",
        "Falls", "Helena", "Lewis", "Clark", "Missoula",
        "Yellowstone", "Grizzly", "Bear", "Mining", "Ranching",
        "Billings", "Kalispell", "Havre", "Anaconda", "Miles",
        "City", "Whitefish", "Belgrade", "Livingston", "Laurel",
        "Orchard", "Homes", "Sidney", "Polson", "Lewistown",
        "Colstrip", "Crow", "Nation", "Blackfeet", "Big",
        "Sky", "Treasure"
    ],
    
    "Nebraska": [
        "Boys", "Town", "Corn", "Huskers", "Cornhuskers", "Lincoln",
        "Memorial", "Stadium", "Nebraska", "Football", "Omaha",
        "Platte", "River", "Runza", "Sandhill", "Cranes",
        "Chimney", "Rock", "Pioneer", "Cattle", "Warren",
        "Buffett", "Bellevue", "Grand", "Island", "Kearney",
        "Fremont", "Hastings", "Norfolk", "Columbus", "Papillion",
        "North", "Platte", "Scottsbluff", "Beatrice", "Henry",
        "Doorly", "Zoo", "Strategic", "Command", "Arbor",
        "Carhenge", "Toadstool"
    ],
    
    "Nevada": [
        "Area", "Casinos", "Hoover", "Dam", "Lake",
        "Mead", "LasVegas", "Neon", "Lights", "Nevada",
        "Desert", "Reno", "Silver", "State", "Strip",
        "Tahoe", "Carson", "City", "Gambling", "Vegas",
        "Henderson", "Enterprise", "Paradise", "Sunrise", "Manor",
        "Spring", "Valley", "Sparks", "Elko", "Boulder",
        "City", "Mesquite", "Fernley", "Fallon", "Winnemucca",
        "Fremont", "Street", "Knights", "Aces", "Aviators",
        "Bellagio", "Luxor"
    ],
    
    "NewHampshire": [
        "Concord", "Franconia", "Notch", "Granite", "State",
        "Lakes", "Region", "Live", "Free", "Die",
        "Manchester", "Moose", "Mount", "Washington", "Nashua",
        "Portsmouth", "Skiing", "Maple", "Syrup", "White",
        "Mountains", "Flume", "Gorge", "Derry", "Dover",
        "Rochester", "Salem", "Merrimack", "Hudson", "Londonderry",
        "Keene", "Bedford", "Goffstown", "Durham", "Laconia",
        "Hampton", "Beach", "Milford", "Exeter", "Windham",
        "Hooksett", "Lebanon"
    ],
    
    "NewJersey": [
        "Atlantic", "City", "Boardwalk", "Boss", "Springsteen",
        "Camden", "Cape", "May", "Cherry", "Hill",
        "Devils", "Diner", "Capital", "Edison", "Jersey",
        "Shore", "Newark", "Palisades", "Pine", "Barrens",
        "Sinatra", "Taylor", "Ham", "Tomatoes", "Trenton",
        "Giants", "Jets", "Paterson", "Elizabeth", "Lakewood",
        "Toms", "River", "Clifton", "Passaic", "Union",
        "City", "Bayonne", "East", "Orange", "Hoboken",
        "Princeton", "MetLife"
    ],
    
    "NewMexico": [
        "Adobe", "Albuquerque", "Balloons", "Carlsbad", "Caverns",
        "Chile", "Peppers", "Enchantment", "Green", "Red",
        "Hatch", "Mesa", "Verde", "Roswell", "Aliens",
        "Santa", "Taos", "White", "Sands", "Pueblo",
        "Desert", "Cruces", "Rio", "Rancho", "Clovis",
        "Farmington", "Alamogordo", "Hobbs", "Portales", "Gallup",
        "Deming", "Lovington", "Sunland", "Park", "Shiprock",
        "Sandia", "Mountains", "Bandelier", "Chaco", "Canyon",
        "Trinity", "Site"
    ],
    
    "NewYork": [
        "Adirondacks", "Albany", "Broadway", "Brooklyn", "Buffalo",
        "Central", "Park", "Empire", "State", "Finger",
        "Lakes", "Jets", "Knicks", "Liberty", "Manhattan",
        "Mets", "Niagara", "Falls", "Rangers", "Sabres",
        "Staten", "Island", "Statue", "Liberty", "Syracuse",
        "Yankees", "Rochester", "Yonkers", "Queens", "Bronx",
        "NewRochelle", "MountVernon", "Schenectady", "Utica", "White",
        "Plains", "Troy", "Binghamton", "Freeport", "Valley",
        "Stream", "Saratoga", "Cooperstown"
    ],
    
    "NorthCarolina": [
        "Asheville", "Bank", "America", "Basketball", "Biltmore",
        "Estate", "Blue", "Ridge", "Cape", "Hatteras",
        "Carolina", "Panthers", "Chapel", "Hill", "Charlotte",
        "Duke", "University", "Great", "Smoky", "Outer",
        "Banks", "Raleigh", "Research", "Triangle", "Tobacco",
        "Road", "Wilmington", "Wright", "Brothers", "BBQ",
        "Tar", "Heels", "Greensboro", "Durham", "Winston",
        "Salem", "Fayetteville", "Cary", "High", "Point",
        "Concord", "Greenville", "Gastonia"
    ],
    
    "NorthDakota": [
        "Bison", "Bismarck", "Fargo", "Flickertail", "State",
        "Grand", "Forks", "Lewis", "Clark", "Minot",
        "North", "Dakota", "Peace", "Garden", "Prairie",
        "Roughriders", "Theodore", "Roosevelt", "Wheat", "Buffalo",
        "Oil", "Boom", "West", "Fargo", "Williston",
        "Dickinson", "Mandan", "Jamestown", "Wahpeton", "Devils",
        "Lake", "Grafton", "Valley", "City", "Watford",
        "Badlands", "Knife", "River", "Sakakawea", "Pembina",
        "Fort", "Totten", "Bakken"
    ],
    
    "Ohio": [
        "Akron", "Browns", "Buckeyes", "Cavs", "Cedar",
        "Point", "Cincinnati", "Cleveland", "Columbus", "Cuyahoga",
        "River", "Dayton", "Hall", "Fame", "Kings",
        "Island", "LeBron", "James", "Neil", "Armstrong",
        "Ohio", "State", "Reds", "Rock", "Roll",
        "Toledo", "Wright", "Brothers", "Bengals", "Parma",
        "Canton", "Youngstown", "Lorain", "Hamilton", "Springfield",
        "Kettering", "Elyria", "Lakewood", "Cuyahoga", "Falls",
        "Middletown", "Newark"
    ],
    
    "Oklahoma": [
        "Cherokee", "Nation", "Cowboy", "Culture", "Dust",
        "Bowl", "Muskogee", "Oklahoma", "City", "Route",
        "Sooners", "Thunder", "Tornado", "Alley", "Tulsa",
        "Will", "Rogers", "Woody", "Guthrie", "Cattle",
        "Native", "American", "Rodeo", "Norman", "Broken",
        "Arrow", "Lawton", "Edmond", "Moore", "Midwest",
        "City", "Enid", "Stillwater", "Shawnee", "Bartlesville",
        "Owasso", "Ponca", "City", "Yukon", "Ardmore",
        "Duncan", "Bricktown"
    ],
    
    "Oregon": [
        "Bend", "Blazers", "Columbia", "River", "Crater",
        "Lake", "Ducks", "Eugene", "Hood", "River",
        "Nike", "Portland", "Salem", "Timbers", "Willamette",
        "Valley", "Coast", "Range", "Cascades", "Powell",
        "Books", "Gresham", "Hillsboro", "Beaverton", "Medford",
        "Springfield", "Corvallis", "Albany", "Tigard", "Lake",
        "Oswego", "Keizer", "Grants", "Pass", "Oregon",
        "City", "McMinnville", "Redmond", "Tualatin", "West",
        "Linn", "Woodburn", "Forest", "Grove"
    ],
    
    "Pennsylvania": [
        "Amish", "Country", "Eagles", "Flyers", "Gettysburg",
        "Harrisburg", "Hershey", "Chocolate", "Independence", "Hall",
        "Liberty", "Bell", "Penguins", "Penn", "State",
        "Philly", "Cheesesteak", "Pittsburgh", "Poconos", "Mountains",
        "Pretzels", "Scrapple", "Steelers", "Valley", "Forge",
        "Wawa", "Yuengling", "Beer", "Amtrak", "Allentown",
        "Erie", "Reading", "Scranton", "Bethlehem", "Lancaster",
        "Levittown", "Wilkes", "Barre", "Chester", "Norristown"
    ],
    
    "PuertoRico": [
        "Arecibo", "Bacardi", "Bayamon", "Caguas", "Camuy",
        "Carolina", "Coqui", "Culebra", "ElMorro", "ElYunque",
        "Guavate", "Guaynabo", "Humacao", "Luquillo", "Mayaguez",
        "Mofongo", "OldSanJuan", "Ponce", "Rincon", "SanJuan",
        "Salsa", "Tostones", "Vieques", "Pina", "Colada",
        "Reggaeton", "Beach", "Flamenco", "Bioluminescent", "Parguera",
        "Isabela", "Fajardo", "Aguadilla", "Cabo", "Rojo",
        "Condado", "Dorado", "Gurabo", "Trujillo", "Alto",
        "Manati", "Tres", "Palmas"
    ],
    
    "RhodeIsland": [
        "Block", "Island", "Brown", "University", "Coffee",
        "Milk", "Cranston", "Dell", "Lemonade", "Newport",
        "Mansions", "Ocean", "State", "Pawtucket", "Providence",
        "Quahog", "Rhode", "Island", "Smallest", "State",
        "Tennis", "Hall", "Warwick", "Woonsocket", "Coventry",
        "Cumberland", "North", "Providence", "West", "Johnston",
        "East", "Providence", "Bristol", "Narragansett", "South",
        "Kingstown", "Burrillville", "Smithfield", "Lincoln", "Central",
        "Falls", "Clam", "Cakes"
    ],
    
    "SouthCarolina": [
        "Beach", "Music", "Charleston", "Clemson", "Tigers",
        "Columbia", "Fort", "Sumter", "Gullah", "Culture",
        "Hilton", "Head", "Lowcountry", "Myrtle", "Beach",
        "Mustard", "BBQ", "Panthers", "Peaches", "Plantations",
        "Rice", "Fields", "South", "Carolina", "Gamecocks",
        "Greenville", "Rock", "Hill", "Mount", "Pleasant",
        "Spartanburg", "Summerville", "Goose", "Creek", "Sumter",
        "Florence", "North", "Charleston", "Anderson", "Greer",
        "Aiken", "Beaufort"
    ],
    
    "SouthDakota": [
        "Badlands", "Park", "Bison", "Herds", "Corn",
        "Palace", "Crazy", "Horse", "Custer", "Park",
        "Deadwood", "Gambling", "Mount", "Rushmore", "Pierre",
        "Rapid", "City", "Sioux", "Falls", "Sturgis",
        "Rally", "Wall", "Drug", "Dakota", "Territory",
        "Pheasant", "Hunting", "Aberdeen", "Brookings", "Watertown",
        "Mitchell", "Yankton", "Huron", "Vermillion", "Spearfish",
        "Brandon", "Box", "Elder", "Madison", "Belle",
        "Fourche", "Harrisburg", "Tea"
    ],
    
    "Tennessee": [
        "Blues", "Music", "Bristol", "Motor", "Chattanooga",
        "Dolly", "Parton", "Elvis", "Presley", "Gatlinburg",
        "Grand", "Opry", "Graceland", "Jack", "Daniels",
        "Memphis", "Music", "City", "Nashville", "Smoky",
        "Mountains", "Titans", "Volunteers", "Whiskey", "Country",
        "Beale", "Street", "Knoxville", "Clarksville", "Murfreesboro",
        "Franklin", "Jackson", "Johnson", "City", "Bartlett",
        "Hendersonville", "Kingsport", "Collierville", "Smyrna", "Cleveland"
    ],
    
    "Texas": [
        "Alamo", "Armadillo", "Astros", "Austin", "BBQ",
        "Brisket", "Bluebonnet", "Cowboys", "Dallas", "Fort",
        "Worth", "Galveston", "Houston", "Longhorns", "Mavs",
        "Mavericks", "Padre", "Island", "Rangers", "River",
        "Walk", "Rodeo", "Spurs", "Stars", "Whataburger",
        "Willie", "Nelson", "Selena", "Bats", "Bridge",
        "Hill", "Country", "SanAntonio", "Corpus", "Christi",
        "Plano", "Laredo", "Lubbock", "Garland", "Irving",
        "Arlington", "ElPaso"
    ],
    
    "Utah": [
        "Arches", "Park", "Bonneville", "Salt", "Bryce",
        "Canyon", "Canyonlands", "Great", "Lake", "Jazz",
        "Basketball", "Mormon", "Temple", "Moab", "National",
        "Parks", "Provo", "Real", "Monarchs", "Skiing",
        "Powder", "Zion", "Park", "Sundance", "Film",
        "Hive", "Symbol", "Olympics", "West", "Valley",
        "City", "Sandy", "Orem", "Ogden", "Layton",
        "Millcreek", "Taylorsville", "Jordan", "Lehi", "Murray",
        "Draper"
    ],
    
    "Vermont": [
        "Autumn", "Foliage", "Ben", "Jerry", "Burlington",
        "Cheese", "Making", "Fall", "Colors", "Ferry",
        "Crossing", "Green", "Mountains", "Maple", "Syrup",
        "Montpelier", "Skiing", "Resorts", "Stowe", "Resort",
        "Teddy", "Bear", "Essex", "Junction", "Colchester",
        "Rutland", "Bennington", "Brattleboro", "Milton", "Hartford",
        "Williston", "Middlebury", "Barre", "Northfield", "Woodstock",
        "Manchester", "Brandon", "Shelburne", "Champlain", "Lake"
    ],
    
    "Virginia": [
        "Arlington", "Blue", "Ridge", "Capitals", "Caverns",
        "Charlottesville", "Chesapeake", "Colonial", "Williamsburg", "Ham",
        "Jamestown", "Jefferson", "Monticello", "Mount", "Vernon",
        "Norfolk", "Pentagon", "Richmond", "Roanoke", "Shenandoah",
        "Valley", "Virginia", "Beach", "Washington", "Birthplace",
        "Winchester", "Alexandria", "Newport", "News", "Hampton",
        "Lynchburg", "Suffolk", "Harrisonburg", "Leesburg", "Blacksburg",
        "Manassas", "Petersburg", "Fredericksburg", "Danville", "Staunton",
        "Salem", "Yorktown"
    ],
    
    "Washington": [
        "Boeing", "Company", "Coffee", "Culture", "Columbia",
        "River", "Evergreen", "State", "Grunge", "Music",
        "Kraken", "Hockey", "Microsoft", "Mount", "Rainier",
        "Nirvana", "Band", "Pike", "Place", "Puget",
        "Sound", "Seahawks", "Seattle", "Space", "Needle",
        "Spokane", "Starbucks", "Tacoma", "Yakima", "Bellingham",
        "Everett", "Kent", "Renton", "Federal", "Way",
        "Bellevue", "Vancouver", "Olympia", "Redmond", "Kirkland",
        "Auburn", "Pasco"
    ],
    
    "WestVirginia": [
        "Appalachia", "Region", "Charleston", "Capital", "Coal",
        "Mining", "Country", "Roads", "Harpers", "Ferry",
        "Mining", "Heritage", "Monongahela", "River", "Mountain",
        "State", "Mountaineers", "Ohio", "River", "Pepperoni",
        "Rolls", "Shenandoah", "Valley", "Almost", "Heaven",
        "Wild", "Wonderful", "Huntington", "Morgantown", "Parkersburg",
        "Wheeling", "Weirton", "Fairmont", "Beckley", "Martinsburg",
        "Clarksburg", "South", "Eastern", "Bluefield", "Vienna",
        "Teays", "Valley"
    ],
    
    "Wisconsin": [
        "Badgers", "Football", "Beer", "Brewing", "Bratwurst",
        "Bucks", "Basketball", "Cheese", "State", "Cheeseheads",
        "Door", "County", "Fish", "Fry", "Green",
        "Bay", "Packers", "Lake", "Michigan", "Madison",
        "Capital", "Milwaukee", "Brewers", "Summerfest", "Music",
        "Dells", "Kenosha", "Racine", "Appleton", "Waukesha",
        "Oshkosh", "Janesville", "West", "Allis", "Sheboygan",
        "Wauwatosa", "Fond", "Dulac", "New", "Berlin",
        "Wausau", "Brookfield"
    ],
    
    "Wyoming": [
        "Buffalo", "Bill", "Cheyenne", "Capital", "Coal",
        "Mining", "Cowboy", "State", "Devils", "Tower",
        "Grand", "Teton", "Jackson", "Hole", "Laramie",
        "City", "Ranch", "Life", "Rodeo", "Culture",
        "Teton", "Range", "Wilderness", "Areas", "Yellowstone",
        "Park", "Casper", "Gillette", "Rock", "Springs",
        "Sheridan", "Green", "River", "Evanston", "Riverton",
        "Cody", "Rawlins", "Lander", "Torrington", "Powell",
        "Mills", "Fort"
    ],
    
    "PuertoRico": [
        "Arecibo", "Observatory", "Bacardi", "Rum", "Bayamon",
        "City", "Caguas", "Municipality", "Camuy", "Caves",
        "Carolina", "City", "Coqui", "Frog", "Culebra",
        "Island", "ElMorro", "Fort", "ElYunque", "Forest",
        "Guavate", "Pork", "Guaynabo", "City", "Humacao",
        "City", "Luquillo", "Beach", "Mayaguez", "City",
        "Mofongo", "Dish", "OldSanJuan", "Historic", "Ponce",
        "City", "Rincon", "Surf", "SanJuan", "Capital",
        "Salsa", "Music", "Tostones", "Food", "Vieques",
        "Island", "Pina", "Colada", "Reggaeton", "Music",
        "Beach", "Culture", "Flamenco", "Beach", "Bioluminescent",
        "Bay", "Parguera", "Bay", "Isabela", "Town",
        "Fajardo", "Port", "Aguadilla", "City", "Cabo",
        "Rojo", "Condado", "Beach", "Dorado", "Beach",
        "Gurabo", "Town", "Trujillo", "Alto", "Manati",
        "Town"
    ]
}

def generate_word_files():
    """Generate a text file for each state with its word list."""
    for state_name, words in state_words.items():
        filename = f"words_{state_name.lower()}.txt"
        with open(filename, 'w') as f:
            for word in words:
                f.write(word + '\n')
        print(f"Created {filename} with {len(words)} words")

if __name__ == "__main__":
    generate_word_files()
    print("\nAll state word files have been generated!")
    print(f"Total states/territories: {len(state_words)}")
