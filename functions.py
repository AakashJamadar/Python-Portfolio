# def greet(name="Guest"):
#     print("Hello "+name)

# # greet("Aakash")
# greet()

# n=5
# for i in range(n,0,-1):
#     print("*"*(i))

# for i in range(n):
#     print("*"*(n-i))

# def sumOfN(n):
#     if n==1: return 1
#     return n+sumOfN(n-1)

# print(sumOfN(44))

# def converter(inch):
#     return inch*2.54
# print(converter(4))

#Write a function to remove the given word from s string and strip it at the same time

def remove_word_and_strip(word,string):
    newStr=string.replace(word,"")
    
    return newStr.strip()

print(remove_word_and_strip("is","   he is a devastating  "))