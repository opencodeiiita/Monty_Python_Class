import csv
import json #for saving the created dictionary as a JSON file


## Function to seperate out the individual genres from the genre column and resturn a list of genres
def seperate_genre(genre_string):
    genre_making=""
    genre_list = []
    for item in genre_string:
        if(item != '|'):
            genre_making = genre_making + item
        elif(item == '|'):
            genre_list.append(genre_making)
            genre_making = ""
        #else:
        #    genre_list.append(genre_making)
        #    genre_making=""
    genre_list.append(genre_making)
    genre_making=""

    return genre_list



result = dict()

path = "movies.csv"

with open(path, "r") as f:
    reader = csv.reader(f)
    next(reader, None)
    for item in reader:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ",item[2])
        genre_list = (seperate_genre(item[2]))
        print(genre_list)
        movie_name = item[1]


        for genre in genre_list:
            if genre in result:
                result[genre].append(movie_name)
            else:
                #add this key to dict
                result[genre] = []
                result[genre].append(movie_name)

print(result)
json = json.dumps(result)
file_handle = open("result.json", "w")
file_handle.write(json)
file_handle.close()





