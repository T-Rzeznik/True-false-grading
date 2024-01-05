

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0 


def getLetter(decimal_grade):
    if decimal_grade > 0.9:
        return "A"
    elif 0.8 <= decimal_grade < 0.9:
        return "B"
    elif 0.7 <= decimal_grade < 0.8:
        return "C"
    elif 0.6 <= decimal_grade < 0.7:
        return "D"
    else :
        return "F"

key = "TFFTFFTTTTFFTFTFTFTT"
     
students_grade = {}


for line in fhand.read().split('\n'):
    if not line:
        continue
    student_ids,answers = line.split(' ', 1)
    score = 0
    for i,letter in enumerate(answers):
        if letter == key[i]:
            score += 1
    students_grade[student_ids] = getLetter(score / len(key))




sortedGrades = sorted([(val,key) for key,val in students_grade.items()], reverse=True)

sortedNames = []
for val,key in sortedGrades:
    sortedNames.append((key,val))

print(sortedNames)
