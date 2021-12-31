with open("InputFiles/Day_10.txt") as f:
    lines = []
    for line in f:
        lines.append(line)

matching_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}

char_error_vals = {')': 3, ']': 57, '}': 1197, '>': 25137}
part_1_ans = 0
for line in lines:
    stack = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif char in [')', ']', '}', '>']:
            opening = stack.pop()
            if matching_chars[opening] != char:
                part_1_ans += char_error_vals[char]
                stack = []
                break
print(part_1_ans)

char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in lines:
    stack = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif char in [')', ']', '}', '>']:
            opening = stack.pop()
            if matching_chars[opening] != char:
                stack = []
                break
    # if there are still opening chars, iterate through backward to find the matching closing chars
    if stack:
        total_score = 0
        for char in stack[::-1]:
            total_score = 5 * total_score + char_scores[matching_chars[char]]
        scores.append(total_score)
part_2_ans = sorted(scores)[len(scores) // 2]
print(part_2_ans)
