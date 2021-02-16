sentence = input().split(" ")
output_sentence = []
for i in range(len(sentence) - 1):
    if sentence[i + 1][0].isupper():
        output_sentence.append(sentence[i] + ".")
    else:
        output_sentence.append(sentence[i])
output_sentence.append(sentence[-1] + ".")
print(" ".join(output_sentence))
