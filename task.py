colorgreen = "\033[1;32m{0}\033[00m"

print colorgreen.format("Task Management System v 1.1 beta")

dictionary = {}

while True:
    task = raw_input("tasks to complete: >>  ")
    yesno = raw_input("task completed yet? (y/n) >>  ")
    print "Your task is: " + task

    if yesno == "y":
        dictionary[task] = True  # task will be included in the dictionary
    else:
        dictionary[task] = False # task will not be included in the dictionary

    yesno2 = raw_input("some more tasks? y/n) >>   ")

    if yesno2 == "n":
        break

print "All tasks: %s" % dictionary
print "END"


file = open("todo.txt", "w+")  # open the TXT file (or create a new one)

print "completed tasks:"
file.write("completed tasks:\n")  # write into the TXT file
for item in dictionary:
    if dictionary[item] == True:
        print "- " + item
        file.write("- " + item + "\n")  # add task into the TXT file

file.write("\n")

print "incomplete tasks:"
file.write("Incomplete tasks:\n")  # write into the TXT file
for item in dictionary:
    if dictionary[item] == False:
        print "- " + item
        file.write("- " + item + "\n")  # add task into the TXT file

file.close()  # close the TXT file