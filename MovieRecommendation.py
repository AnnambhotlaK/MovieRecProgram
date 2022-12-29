# This program will suggest critically acclaimed movies of a specific genre to the user.
# Data is stored in a HashTable.
# It also features autocomplete for convenience.

from HashTable.py import *
from MovieData.py import *

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
# For example, a search for "a" may return ["action", "fantasy", "drama", "romance"]
# Followed by "ac" returns only ["action"], the desired genre
def search(options, searchLength):
    newOptions = [] # Where the next set of options will go

    search = input("Please enter the first character of the genre of your choice: ")
    while len(search) != searchLength:
        print("Sorry, we don't understand the input.")
        search = input("Please enter the first character of the genre of your choice: ")

    #if options == None:
        #options = movies.keys()

    for genre in options:
        if search in genre[0:searchLength]:
            newOptions.append(genre)
    
    searchLength += 1
    options = newOptions

    if len(options) > 1: # Still not narrowed down
        #print(type(options))
        #print(type(searchLength))
        print("With this input, the possible genres are: " + options)
        return search(options, searchLength)
    elif len(options) == 1: # Only one remaining; returns list of length 1 that has correct option
        print("With this input, we believe your genre of choice is: " + "".join(options))
        check = input("Is this correct? Enter y/n: ")
        if check == 'y':
            return options
        elif check == 'n':
            print("Sorry! Please try again...")
            return search(movies.keys(), 1)
        else:
            print("Sorry, we didn't understand that. Please search again.")
            return search(movies.keys(), 1)
    else: # Did not work
        print("Sorry, we could not find the genre of your choice.")
        return search(movies.keys(), 1)

# Prints formatted output of movies based on genre
def output(genre):
    moviesInGenre = movies[genre] # 2d array

    for movie in moviesInGenre: # each movie in the genre
        print("---------------------------------------------------------")
        print("Title: " + movie[0])
        print("Director: " + movie[1])
        print("Release Year: " + movie[2])
        print("IMDb Rating: " + movie[3])
    print("---------------------------------------------------------")

    


# Master function, contains running logic
def run():
    greet()
    genre = "".join(search(movies.keys(), 1)) # Selection as a string
    output(genre)
    repeat = input("Would you like to look for more movies? Enter y/n: ")
    while (repeat == 'y'):
        genre = "".join(search(movies.keys(), 1))
        output(genre)
        repeat = input("Would you like to look for more movies? Enter y/n: ")
        while (repeat != 'y' or repeat != 'n'):
            repeat = input("Would you like to look for more movies? Enter y/n: ")

    print("Thank you for coming!")

run()


