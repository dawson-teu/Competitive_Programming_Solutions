n = int(input())
processors = [[int(num) for num in input().split(" ")] for i in range(n)]
for processor in processors:
    if processor[0] * processor[1] == processor[2]:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")
