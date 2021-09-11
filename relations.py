import requests

universalMoviesList = []

genresDict = {
    "Comedy": [],
    "Fantasy": [],
    "Crime": [],
    "Drama": [],
    "Music": [],
    "Adventure": [],
    "History": [],
    "Thriller": [],
    "Animation": [],
    "Family": [],
    "Mystery": [],
    "Biography": [],
    "Action": [],
    "Film-Noir": [],
    "Romance": [],
    "Sci-Fi": [],
    "War": [],
    "Western": [],
    "Horror": [],
    "Musical": [],
    "Sport": [],
}

# Fetching the movies data from the url and getting the json object
moviesApiRequest = requests.get('https://raw.githubusercontent.com/erik-sytnyk/movies-list/master/db.json')
moviesJSON = moviesApiRequest.json()

# Looping through the json object to append into relevant genre arrays
for movie in moviesJSON['movies']:
    universalMoviesList.append(movie['title'])
    for genre in movie['genres']:
        genresDict[genre].append(movie['title'])


# Creating 3 list of sets from index 0 to 2
setA = list(genresDict.values())[0]
setB = list(genresDict.values())[1]
setC = list(genresDict.values())[2]

setAB = []
setAC = []

# Looping through setA and setB to create relation map
for movieA in setA:
    for movieB in setB:
        setAB.append((movieA, movieB))

# Looping through setA and setC to create relation map
for movieA in setA:
    for movieB in setC:
        setAC.append((movieA, movieB))

# Check if two sets are function
def isFunction(R):
    for a in R:
        count = 0
        for b in R:
            if (a[0] == b[0]):
                count += 1
                if (count > 1):
                    print("Not a function")
                    return False
        print("A function")
        return True


# Function to check if the set is Reflexive
def isReflexive(R, A):
    for a in A:
        if (a, a) not in R:
            print("Not reflexive")
            return False
    print("Reflexive")
    return True

# Function to check if the set is Symmetric
def isSymmetric(R, A):
    for a, b in R:
        if (b, a) not in R:
            print("Not Symmetric")  
            return False
    print("Symmetric")            
    return True

# Function to check if the set is Transitive
def isTransitive(R, A):
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        print("Not Transitive")
                        return False
    print("Transitive")
    return True

# Checking if a set is function
isFunction(setAB)
isFunction(setAC)

# Checking reflexive, symmetric and transitive for setAB
isReflexive(setAB, setA)
isSymmetric(setAB, setA)
isTransitive(setAB, setA)

# Checking reflexive, symmetric and transitive for setAC
isReflexive(setAC, setA)
isSymmetric(setAC, setA)
isTransitive(setAC, setA)