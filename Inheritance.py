class Dog:
    breed = "Specific Dog breed"  # Parent Class #
    spayed = "Enter Y or N"
    tagged = "Enter Y or N"
    tag_number = "Enter Tag Number" 

class Sheltered(Dog): # Child Class #
    shelter_location = 'Enter location of Shelter'
    shelter_ID = 'Enter ID number of specific shelter'
    tag_number = "Enter Tag Number"

class Missing(Dog): # Child Class #
    location = "Enter last location dog was seen"
    date = "Enter last date dog was seen"
    time = "Enter time dog was last seen on last date"
    
    
    
