#Football Quiz
import fileinput
import time
a = []
b = []
#For total correct answer
count = 0
# Total 3 Life
life = 3
# To add all the line in the file into list
for questions in fileinput.input(files = 'footballquiz.txt'):
    a.append(questions)
for answers in fileinput.input(files = 'quizanswers.txt'):
    b.append(answers)
#Comapring Answer
for i in range(0, len(a)):
    print(a[i])
    print("Enter Your Answer: ")
    c = input()
    if (b[i]).upper() == (c + '\n').upper():
        print("Correct")
        time.sleep(2)
        print()
        count = count + 1
    else:
        print("Incorrect")
        print("Correct Answer was: ", b[i])
        time.sleep(2)
        print()
        life = life - 1
        time.sleep(2)
        print("Total Life remaning: ", life)
        print()
        time.sleep(2)
        print()
        if life == 0:
            time.sleep(2)
            print("""
            ***************
            **|GAME OVER|**
            ***************""")
            time.sleep(2)
            break
time.sleep(2)
print("Total Correct answer: ", count, "Out of 25")
d = (count/25)*100
time.sleep(2)
print("Percentage: ", d)
time.sleep(5)
if d >= 90:
    print("GREAT")
elif d >= 80:
    print("Good")
elif d >= 60:
    print("Average")
elif(d >= 40 and d < 60):
    print("Basic")
else:
    print("Very Poor")
time.sleep(2)
print()
