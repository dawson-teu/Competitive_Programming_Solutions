# Only use if input is too large to buffer
# import sys
# input = sys.stdin.readline

# For fast input from a text file
# If input is small lines can be buffered or otherwise used in place
# with open("put_file_here.txt") as f:
#     for line in f:
#         print(line)

import sys
data = sys.stdin.read().split('\n')
