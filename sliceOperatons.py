#           module 
# import os
# print(os.listdir())

# a=None

#slice operations

text = "Python"
# print(text[::-1])  # Reverses the entire string: "nohtyP"
# print(text[4:0:-1])  # Prints "ohty"
print(text[-1::-1])
print(text[0:65:-1])
#if i keep space before the word print it doesn't run

#date=31-07-2024

#conclusion:with no step the default is 1 so it jumps(not skip but jump on it) a step of 1 everytime,so if i have 4:0 it starts from 4
#and start jumping one step forward and i cannot reach 0 ever
#In the same way,if step has -1 we jump one step reverse,so if i has 0:4:-1, it starts from 0 and jumps one step back and can never 
#find the 4th index

#conclusion:if the step index is 1 we move right if it is -1 we move left

# Excellent question. Let's break down how Python's slice notation [a:b:c] behaves when we omit different parts:

# When we leave a (start index):

# If c is positive or omitted: a defaults to 0
# If c is negative: a defaults to the end of the string (-1)


# When we leave b (stop index):

# If c is positive or omitted: b defaults to the length of the string
# If c is negative: b defaults to the beginning of the string (before index 0)(we can say -length too but befors 0 is conceptually accurate)


# When we leave c (step):

# c always defaults to 1

print(text[-4:1:-1])

# arr = 'PrepInsta'
# print(arr[1:7:3])