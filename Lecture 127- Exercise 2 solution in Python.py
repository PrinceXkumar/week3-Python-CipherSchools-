# users = { 
# 'name' : 'Harshit'

# 'age' : 24,

# 'fav_movies' : ['coco', 'avengers']

# fav_songs' : ['songl', 'song2']

#1}

user = {}

name = input('What is your name : ')

age = input('what is your age : ')

fav_movies = input('fav movies Separated by , ').split(',')
fav_songs = input('your fav songs separated by , ').split(',')
user['name'] = name

user['age'] = age

user['fav_movies'] = fav_movies
#print(user)

for key, value in user.items():
    print(f"{keys} : {value}")