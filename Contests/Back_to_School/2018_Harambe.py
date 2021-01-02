original = input()
student = input()
k = int(input())

count = 0
for i in range(len(original)):
    if (original[i] == " " and not student[i] == " ") or (student[i] == " " and not original[i] == " "):
        count = 1001
        break
    if not original[i] == student[i]:
        count += 1
if count <= k:
    print("Plagiarized")
else:
    print("No plagiarism")
