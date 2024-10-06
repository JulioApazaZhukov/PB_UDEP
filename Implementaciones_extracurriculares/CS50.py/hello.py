import sys

name = input("Name: ")

print("Hello,", name)       # "," automatically creates a space
print("Hello, " + name)     # "+" does not automatically create a space
print(f"Hello, {name}")     # fancy alternative

number  = int(input("Number: "))

if number > 0:
    print("Positive number")
elif number == 0:
    print("Number = 0")
else:
    print("Negative number")

base = int(input("Base: "))
exponent = int(input("Exponent: "))

def exponentiation(n, e):
    r = n
    while e > 1:
        r = r*n
        e = e-1
    return r
print(exponentiation(base, exponent))

array = ["1", "2", "3"] # Lists = Arrays
print(array)
array.append("five")
print(array)

s = set() # Data type similar to lists, but without repetitions

s.add(1)
s.add(2)
s.add(3)
s.add(2)

print(s)        # No repeating elements

print(f"The set has {len(s)} elements")

for i in range(0, 11, 2):       # ... in range(start, stop, step):
    print(i)

#Dictionaries: key:value
capitals = {"Peru": "Lima", 
            "Russia": "Moscow",
            "Argentina": "Buenos Aires"}

print(capitals["Peru"])

# OOP
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():                   # if not self.open_seats(): => if self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Albert", "Immanuel", "Josh", "Dennis"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")

def announce(f):
    def wrapper():
        print("Abbout to run the function...")
        f()
        print("Done whith the function.")
    return wrapper
@announce
def hello():
    print("Hello, world!")
hello()

# lambda
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def funct(person):
    return person["name"]

people.sort(key=funct)
print(people)

# Exeptions (8.1.py, 8.2.py)
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Only numbers accepted.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot devide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")