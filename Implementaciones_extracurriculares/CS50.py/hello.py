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

array = ["1", "2", "3"]
print(array)
array.append("five")
print(array)

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(2)

print(s)        # No repeating elements

print(f"The set has {len(s)} elements")

for i in range(0, 11, 2):       # ... in range(start, stop, step):
    print(i)

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