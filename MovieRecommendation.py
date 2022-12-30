# This program will suggest critically acclaimed movies of a specific genre to the user.
# It also features autocomplete for convenience.

from HashTable import *
from MovieData import *

# Create the hashmap:
movies = HashTable(9) # For nine genres
movies.setVal("action", actionMovies)
movies.setVal("comedy", comedyMovies)
movies.setVal("drama", dramaMovies)
movies.setVal("fantasy", fantasyMovies)
movies.setVal("horror", horrorMovies)
movies.setVal("mystery", mysteryMovies)
movies.setVal("romance", romanceMovies)
movies.setVal("thriller", thrillerMovies)
movies.setVal("western", westernMovies)

movieKeys = ["action", "comedy", "drama", "fantasy", "horror", "mystery", "romance", "thriller", "western"]

# Opening greeting/introduction
def greet():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("* * * * WELCOME TO THE MARVELOUS MOVIE STORE! * * * *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print()
    print("   This establishment features a variety of  ")
    print("   critically-acclaimed films from nine of   ")
    print("  the most popular genres ever. It also uses ")
    print(" advanced autocomplete to predict the genre of")
    print("    your choice with only a few characters.")
    print()
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")

# Search system. Accepts array of options, returns an array of options. 
def search(options, searchLength):
    
    # There are options remaining
    while (len(options) > 1):

        newOptions = []

        search = input("Please search for the genre of your choice: ")
        # User did not enter a search of valid length
        while (len(search) == 0 or len(search) > searchLength):
            print("Sorry, we didn't understand that.")
            search = input("Please search for the genre of your choice: ")
        # Otherwise, the search was good, and we can begin narrowing down options:

        for genre in options:
            if search in genre[0:searchLength]:
                newOptions.append(genre)
        # By end of for loop, we have all valid options remaining
        # Increase valid search length:
        searchLength += 1
        # And update options:
        options = newOptions
    
    # If we're out of the while loop, that means one of two things:
    # We have no options and must alert the user...

    if len(options) == 0:
        print("Sorry, we do not have the genre of your choice.")
        return None
    
    # Or we have one option (perfect!)
    print("We have narrowed your search down to one genre: " + "".join(options))
    check = input("Is this correct? Enter y/anything else: ")
    if check == 'y':
        print("Here's your albums!")
        return "".join(options)
    else:
        print("Our apologies for failing to find your search. Please search again.")
        return None

# Prints formatted output of movies based on genre
def output(genre):
    moviesInGenre = movies.getVal(genre) # 2d array

    for movie in moviesInGenre: # each movie in the genre
        print("---------------------------------------------------------")
        print("Title: " + movie[0])
        print("Director: " + movie[1])
        print("Release Year: " + movie[2])
        print("IMDb Rating: " + movie[3])
    print("---------------------------------------------------------")

    


# Master function, contains running logic
def run():
    
    # Allows for repetition
    repeat = 'y'
    greet() # Welcome message

    while (repeat == 'y'):

        genre = search(movieKeys, 1)

        # User did not find genre of choice, have them retry
        while genre == None:
            genre = search(movieKeys, 1)

        # Otherwise, we can output
        output(genre)

        # Ask user if they want to continue
        repeat = input("Would you like to look for more movies? Enter 'y'/anything else: ")

    # Prints when user said definitive "no"
    print("Thank you for coming!")

# Run program!
run()








