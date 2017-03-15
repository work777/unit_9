# Your friend was so happy with your program that he told everyone how great programmer
# you are. A nearby restaurant owner heard about this and immediately contacted you.
# He'd like to have a program where he'd enter their daily menu and it would get saved
# into a menu.txt file. The menu would consist of a dish (like "Beef steak with potatoes"
# and a price of the dish (e.g. 5.40). When you finish, push your code on GitHub and share
# it on the SmartNinja forum.

print
print "Welcome to Smart Meal Text Output System v.1.0"
print "=============================================="

file = open("restaurant.txt", "w+")
file.write("Menu for today: ")
file.write("\n" + "\n")

list = {}

while True:
    meal = raw_input("Enter meal >> ")
    price = raw_input("Enter price >> ")
    list[meal] = True
    list[price] = True

    file.write(meal + " ............................ ")
    file.write(price + "\n")

    q = raw_input("more meals? (y/n) >> ")
    if q == "n":
        break









