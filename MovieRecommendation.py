# This program will suggest critically acclaimed movies of a specific genre to the user.
# It also features autocomplete for convenience.

# ------------- LIST OF MOVIES START -------------

# Action Movies:
sevenSamurai = ["'Seven Samurai'", "Akira Kurosawa", "1954", "8.6"]
empireStrikesBack = ["'Star Wars: Episode V - The Empire Strikes Back'", "Irvin Kershner", "1980", "8.7"]
theMatrix = ["'The Matrix'", "The Wachowskis", "1999", "8.7"]
gladiator = ["'Gladiator'", "Ridley Scott", "2000", "8.5"]
theDarkKnight = ["'The Dark Knight'", "Christopher Nolan", "2008", "9.0"]
actionMovies = [sevenSamurai, empireStrikesBack, theMatrix, gladiator, theDarkKnight]

# Comedy Movies:
drStrangelove = ["'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb'", "Stanley Kubrick", "1964", "8.4"]
montyPython = ["'Monty Python and the Holy Grail'", "Terry Gilliam, Terry Jones", "1975", "8.2"]
groundhogDay = ["'Groundhog Day'", "Harold Ramis", "1993", "8.1"]
bigLebowski = ["'The Big Lebowski'", "The Coen Brothers", "1998", "8.1"]
littleMissSunshine = ["'Little Miss Sunshine'", "Jonathan Dayton, Valerie Faris", "2006", "7.8"]
comedyMovies = [drStrangelove, montyPython, groundhogDay, bigLebowski, littleMissSunshine]

# Drama Movies:
casablanca = ["'Casablanca'", "Michael Curtiz", "1942", "8.5"]
theGodfather = ["'The Godfather'", "Francis Ford Coppola", "1972", "9.2"]
amadeus = ["'Amadeus'", "Milos Forman", "1984", "8.4"]
shawshankRedemption = ["'The Shawshank Redemption'", "Frank Darabont", "1994", "9.3"]
inception = ["Inception", "Christopher Nolan", "2010", "8.8"]
dramaMovies = [casablanca, theGodfather, amadeus, shawshankRedemption, inception]

# Fantasy Movies:
wizardOfOz = ["'The Wizard of Oz'", "Victor Fleming", "1939", "8.1"]
beautyAndTheBeast = ["'The Beauty and the Beast'", "Jean Cocteau", "1946", "7.9"]
princessBride = ["'The Princess Bride'", "Rob Reiner", "1987", "8.0"]
returnOfTheKing = ["'The Lord of the Rings: The Return of the King'", "Peter Jackson", "2003", "9.0"]
deathlyHallowsTwo = ["'Harry Potter and the Deathly Hallows: Part 2'", "David Yates", "2011", "8.1"]
fantasyMovies = [wizardOfOz, beautyAndTheBeast, princessBride, returnOfTheKing, deathlyHallowsTwo]

# Horror Movies:
psycho = ["'Psycho'", "Alfred Hitchcock", "1960", "8.5"]
exorcist = ["'The Exorcist'", "William Friedkin", "1973", "8.1"]
shining = ["'The Shining'", "Stanley Kubrick", "1980", "8.4"]
silenceOfTheLambs = ["'The Silence of the Lambs'", "Jonathan Demme", "1991", "8.6"]
getOut = ["'Get Out'", "Jordan Peele", "2017", "7.7"]
horrorMovies = [psycho, exorcist, shining, silenceOfTheLambs, getOut]

# Mystery Movies:
citizenKane = ["'Citizen Kane'", "Orson Welles", "1941", "8.3"]
rearWindow = ["'Rear Window'", "Alfred Hitchcock", "1954", "8.5"]
chinatown = ["'Chinatown'", "Roman Polanski", "1974", "8.2"]
se7en = ["'Se7en'", "David Fincher", "1995", "8.6"]
memento = ["'Memento'", "Christopher Nolan", "2000", "8.4"]
mysteryMovies = [citizenKane, rearWindow, chinatown, se7en, memento]

# Romance Movies:
soundOfMusic = ["'The Sound of Music'", "Robert Wise", "1965", "8.1"]
whenHarryMetSally = ["'When Harry Met Sally...'", "Rob Reiner", "1989", "7.7"]
titanic = ["'Titanic'", "James Cameron", "1997", "7.9"]
eternalSunshine = ["'Eternal Sunshine of the Spotless Mind'", "Michel Gondry", "2004", "8.3"]
slumdogMillionaire = ["'Slumdog Millionaire'", "Danny Boyle", "2008", "8.0"]
romanceMovies = [soundOfMusic, whenHarryMetSally, eternalSunshine, slumdogMillionaire]

# Thriller Movies:
nightOfTheHunter = ["'The Night of the Hunter'", "Charles Laughton", "1955", "8.0"]
deliverance = ["'Deliverance'", "John Boorman", "1972", "7.7"]
misery = ["'Misery'", "Rob Reiner", "1990", "7.8"]
changeling = ["'Changeling'", "Clint Eastwood", "2008", "7.8"]
shutterIsland = ["'Shutter Island'", "Martin Scorsese", "2010", "8.2"]
thrillerMovies = [nightOfTheHunter, deliverance, misery, changeling, shutterIsland]

# Western Movies:
highNoon = ["'High Noon'", "Fred Zinnemann", "1952", "8.0"]
goodBadUgly = ["'The Good, the Bad and the Ugly'", "Sergio Leone", "1966", "8.8"]
joseyWales = ["'The Outlaw Josey Wales'", "Clint Eastwood", "1976", "7.8"]
unforgiven = ["'Unforgiven'", "Clint Eastwood", "1992", "8.2"]
django = ["'Django Unchained'", "Quentin Tarantino", "2012", "8.4"]
westernMovies = [highNoon, goodBadUgly, joseyWales, unforgiven, django]

# Hashmap used to store data and draw values from.
# each genre key (string) points to a list of movies value (two-dimensional array).
movies = { "action" : actionMovies, "comedy" : comedyMovies, "drama" : dramaMovies, 
"fantasy" : fantasyMovies, "horror" : horrorMovies, "mystery" : mysteryMovies, 
"romance" : romanceMovies, "thriller" : thrillerMovies, "western" : westernMovies }

# ------------- LIST OF MOVIES END -------------

# Opening greeting/introduction
def greet():
    print("* * * * * * * * * * * * * * * * * * * * * * *")
    print("* * WELCOME TO THE MARVELOUS MOVIE STORE! * *")
    print("* * * * * * * * * * * * * * * * * * * * * * *")
    print()
    print("   This establishment features a variety of  ")
    print("   critically-acclaimed films from nine of   ")
    print("  the most popular genres ever. It also uses ")
    print(" advanced autocomplete to predict the genre of")
    print("    your choice with only a few characters.")
    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - ")

# Search system. Accepts array of options, returns an array of options. 
# For example, a search for "a" may return ["action", "fantasy", "drama", "romance"]
# Followed by "ac" returns only ["action"], the desired genre
def search(options, searchLength):
    newOptions = [] # Where the next set of options will go

    search = input("Please enter the first character of the genre of your choice: ")
    while len(search) != searchLength:
        print("Sorry, that is not specific enough!")
        search = input("Please enter the first character of the genre of your choice: ")

    if options == None:
        options = movies.keys()

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
            return search(None, 1)
        else:
            print("Sorry, we didn't understand that. Please search again.")
            return search(None, 1)
    else: # Did not work
        print("Sorry, we could not find the genre of your choice.")
        return search(None, 1)

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
    genre = "".join(search(None, 1)) # Selection as a string
    output(genre)
    repeat = input("Would you like to look for more movies? Enter y/n: ")
    while (repeat == 'y'):
        genre = "".join(search(None, 1))
        output(genre)
        repeat = input("Would you like to look for more movies? Enter y/n: ")
        while (repeat != 'y' or repeat != 'n'):
            repeat = input("Would you like to look for more movies? Enter y/n: ")

    print("Thank you for coming!")

run()








