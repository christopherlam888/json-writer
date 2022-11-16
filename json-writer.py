print("Welcome to JSON Writer!")
filename = input("Enter the name of the file to write: ").strip() + ".json"
try:
    file = open(filename, "x")
except:
    print("File already exists.")
    quit()
fields = []
data = []
userInput = "y"
while userInput == "y" or userInput == "Y":
    fields.append(input("Enter a data field: ").strip())
    userInput = input("Add another field? Enter y or Y to continue or any other key to finish. ").strip()
userInput = "y"
while userInput == "y" or userInput == "Y":
    entry = []
    for i in range(len(fields)):
        entry.append(input(f"{fields[i]}: ").strip())
    data.append(entry)
    userInput = input("Add another entry? Enter y or Y to continue or any other key to finish. ").strip()
file.write("[\n")
for i in range(len(data)):
    file.write("\t{\n")
    for j in range(len(fields)):
        file.write(f"\t\t\"{fields[j]}\": \"{data[i][j]}\"")
        if j != len(fields)-1:
            file.write(",")
        file.write("\n")
    file.write("\t}")
    if i != len(data)-1:
        file.write(",")
    file.write("\n")
file.write("]\n")
file.close()
print("File written!\n")
