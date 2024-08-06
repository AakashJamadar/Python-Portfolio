# n=5
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"*n)
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*")

  
num=int(input("Enter a number"))

# for i in range(1,11):
#     #print(str(num)+"X"+str(i)+"="+str(num*i))
#     #other way
#     print(F"{num}X{i}={num*i}")   #keep variable names inside {}

# for i in range(10,0,-1):
#     print(f"{num}X{i}={num*i}")

# for i in reversed(range(1,11)):
#     print(f"{num}X{i}={num*i}")

#using while loop
i=10
while i>0:
    print(f"{num}X{i}={num*i}")
    i-=1