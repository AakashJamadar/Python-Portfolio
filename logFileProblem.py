#Write a program to mine a log file and find out whether it contains 'python'

# with open("log.txt") as f:
#     content=f.read().lower()
# if 'python' in content:
#     print("python is present")
# else:
#     print("python is not present")
# Now find out the line number where 'python' is present

i=1
with open("log.txt") as f:  
    content=True
    while content: 
        content=f.readline().lower()    #returns empty string after the lines are finished,empty string is false as we know
        if 'python' in content:
            print(f"python is present on line number {i}")
        i+=1