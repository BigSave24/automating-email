
# File operations
file = open("./data/exam.csv", "r")

for line in file.readlines():
    print(line)
