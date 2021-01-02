n = int(input())
student = []
for i in range(n):
    student.append(input())
answers = []
for i in range(n):
    answers.append(input())

total = 0
for i in range(n):
    if student[i] == answers[i]:
        total += 1
print(total)
