people =[
    {"name" : "harry", "house" : "gryffindor"},
    {"name" : "ron", "house" : "ravenclaw"},
    {"name" : "hermione", "house" :"slytherin"},
    {"name" : "draco", "house" : "hufflepuff"},
]


people.sort(key= lambda person : person["name"])

print(people)