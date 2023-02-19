# STRINGS
name= "harry"

print(name[0])
print(name[1])
print(name[2])

# LISTS
names=["harry", "ron", "hermione"]

# append items to list
names.append("kartik")

# sorting list
names.sort()


print(names)
print(names[0])
print(names[1])

# SETS
s=set()

s.add(1)
s.add(7)
s.add(6)
s.add(3)
s.add(4)
s.add(5)
s.add(4)
s.add(3)
s.add(2)

print(s)

s.remove(4)

# Defining a dictionary
house = {"harry":"gryffindor", "ron":"slytherin", "hermione":"hufflepuff"}

# adding a new key
house["draco"] = "slytherin"

# printing dict
print(house)
print(house["draco"])

# LOOPS
# for loop

for i in range(6):
    print(i)

ab= "harry"

for char in ab:
    print(char)