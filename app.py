from os import wait
import smtplib
import random
import time


print("Enter Filename: ")
file_name = input()
lookup = {}
randomStudent = ''


def studentScores(fileName):

    # File operations
    file = open("./data/" + fileName, "r")

    for line in file.readlines():
        keys = line.split(',')
        lookup.update({keys[0]: {
            'email': keys[0],
            'lastName': keys[1],
            'firstName': keys[2],
            'problem_1_score': keys[3],
            'problem_1_comments': keys[4],
            'problem_2_score': keys[5],
            'problem_2_comments': keys[6],
            'problem_3_score': keys[7],
            'problem_3_comments': keys[8].rstrip()
        }})

    mailList = [x for x in lookup.keys()]
    randomStudent = random.choice(mailList)


def sendEmail(studentList):

    # Setup SMTP server
    server = smtplib.SMTP_SSL('smtp.provider.com', 465)
    server.login("username@domain.com", "pw")
    server.set_debuglevel(1)

    for student in studentList:
        from_addr = 'teacher@example.com'
        to_addrs = studentList[student]['email']

        if studentList[student]['email'] == randomStudent:
            msg = (
                f"Subject: Score Report for {studentList[student]['firstName']}\n"
                f"Dear {studentList[student]['firstName']},\n\n"

                f"Your score for the book assignment is broken down below by question number.\n\n"

                f"1. {studentList[student]['problem_1_score']}%: {studentList[student]['problem_1_comments']}\n"
                f"2. {studentList[student]['problem_2_score']}%: {studentList[student]['problem_2_comments']}\n"
                f"3. {studentList[student]['problem_3_score']}%: {studentList[student]['problem_3_comments']}\n\n"

                f"You/’ve been randomly chosen to present a summary of the book in the next class. Looking forward to it!\n"
            )
        else:
            msg = (
                f"Subject: SMTP e-mail test\n"
                f"Dear {studentList[student]['firstName']},\n\n"

                f"Your score for the book assignment is broken down below by question number.\n\n"

                f"1. {studentList[student]['problem_1_score']}%: {studentList[student]['problem_1_comments']}\n"
                f"2. {studentList[student]['problem_2_score']}%: {studentList[student]['problem_2_comments']}\n"
                f"3. {studentList[student]['problem_3_score']}%: {studentList[student]['problem_3_comments']}\n"
            )

        server.sendmail(from_addr, to_addrs, msg)
        # Wait 1 second to send next email
        time.sleep(1)

    server.quit()


studentScores(file_name)
sendEmail(lookup)
