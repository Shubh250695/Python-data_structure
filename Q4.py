# Q4  Write a Python program to replace last value of tuples in a list.

# Sample list: [(10, 20, 30), (40, 50, 90), (70, 80, 60)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

sample_list = [(10, 20, 30), (40, 50, 90), (70, 80, 60)]

print ("Given list :", sample_list)

for i in range (len (sample_list)):
    sample_list[i] = list (sample_list[i])
    sample_list[i][-1] = 100
    sample_list[i] = tuple (sample_list[i])
print ("Output list :",sample_list)