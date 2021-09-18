import smtplib
import random

print("Enter Filename: ")
file_name = input()
lookup = {}


def studentScores(fileName):

    # File operations
    file = open("./data/" + fileName, "r")

    for line in file.readlines():
        keys = line.split(',')
        lookup.update({keys[0]: {
            'Email': keys[0],
            'lastName': keys[1],
            'firstName': keys[2],
            'problem_1_score': keys[3],
            'problem_1_comments': keys[4],
            'problem_2_score': keys[5],
            'problem_2_comments': keys[6],
            'problem_3_score': keys[7],
            'problem_3_comments': keys[8].rstrip()
        }})

    print(lookup)
    randomStudent(lookup)


def randomStudent(studentData):
    emailList = [x for x in studentData.keys()]
    idx = random.randint(0, len(emailList))

    print(emailList)
    print(emailList[idx])
    return emailList[idx]


studentScores(file_name)
