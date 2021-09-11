import requests
import json
import array
import math

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

# Sorting genres with most movies
genreList = sorted(genresDict, key=lambda l: (len(l), l))

# Union of the movies from top three genres
unionMovieListAB = list(set().union(genresDict[genreList[0]], genresDict[genreList[1]]))
unionMovieListBC = list(set().union(genresDict[genreList[1]], genresDict[genreList[2]]))
unionMovieListAC = list(set().union(genresDict[genreList[0]], genresDict[genreList[2]]))

# Intersection of the movies from top three genres
intersectMovieListAB = list(set(genresDict[genreList[0]]) & set(genresDict[genreList[1]]))
intersectMovieListBC = list(set(genresDict[genreList[1]]) & set(genresDict[genreList[2]]))
intersectMovieListAC = list(set(genresDict[genreList[0]]) & set(genresDict[genreList[2]]))

print(intersectMovieListAB)
print(intersectMovieListBC)
print(intersectMovieListAC)

# Compliments of the movies from top three genres

complimentMovieListA = list(set(universalMoviesList) - set(genresDict[genreList[0]]))
complimentMovieListB = list(set(universalMoviesList) - set(genresDict[genreList[1]]))
complimentMovieListC = list(set(universalMoviesList) - set(genresDict[genreList[2]]))

print(complimentMovieListA)
print(complimentMovieListB)
print(complimentMovieListC)


def computePowerSet(setData):
    print(setData[0])
    setSize = len(setData)
    powerSize = (int) (math.pow(2, setSize))
    print(powerSize, "\n")
    counter = 0
    j = 0
     
    for counter in range(0, powerSize):
        newSet = []
        for j in range(0, setSize):
            if((counter & (1 << j)) > 0):
                newSet.append(setData[j])
        print(newSet)
 

computePowerSet(list(genresDict[genreList[0]]))