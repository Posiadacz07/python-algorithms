# Problem: Dutch National Flag problem
#          - sort an array of 0s, 1s and 2s.
# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
#
# Example:
# Input:
# 0 2 1 2 0
# Output: 
# 0 0 1 2 2


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# sorting array
sort_arr = arr
sort_arr.sort()

print(sort_arr)

# counting 0s, 1s and 2s
count_arr = []
zeros = 0
ones = 0
twos = 0

# for a in arr:
#     if a == 0:
#         zeros += 1
#     elif a == 1:
#         ones += 1
#     elif a == 2:
#         twos +=1

for a in arr:
    match a:
        case 0:
            zeros += 1
        case 1:
            ones += 1
        case 2:
            twos +=1

while(zeros > 0):
    count_arr.append(0)
    zeros -= 1
while(ones > 0):
    count_arr.append(1)
    ones -= 1
while(twos > 0):
    count_arr.append(2)
    twos -= 1

print(count_arr)