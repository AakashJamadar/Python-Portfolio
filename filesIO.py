# #use open function to read the content of a file
# #file=open('sample.txt','r')
# file=open("sample.txt")     # by default, the mode is 'r'(read mode)
# data=file.read()
# #data=file.read(10)          # reads the first 10 characters from the file,,cannot read twice so erased the upper .read()
# print(data)
# file.close()

#  ,readline() function ,,,,reads a one full line ata time
# f=open('sample.txt')
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
#f.close()      #don't forget this
#  new lines are getting printed each time because of the newline character after the endline of a file as well as from the print function

# Modes of opening a file

# r ->open forr reading
# w ->open for writing
# a ->open for appending
# + ->open for updating

# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode  #t is added by default

#Writing files in python

# f=open("another.txt",'w')   #it automatically creates the file another.txt if the file doesn't exist
# f.write("Hello ")
# f.write("g")       #this adds the text after the pervious text without space
# f.write("dsf")
# #   if i change the mode to 'a'(append) and use write ,it keeps on adding the text at the end after every successful program run
# f.close()   #see potential issues of not closing the file
#erases the previous text before writing new text in write mode
# running the above code doesn't write the content multiple times like it happens in append mode

#Differences between the write and append mode
#write mode erases the previous text unlike append which adds the content to the end

# f=open("another.txt",'a')
# data=f.write("\nI am appending")        #using '\n at the beginning writes the content in a new line
# print(data)

# 14 is getting printed because the write method writes the content to the filw also eturning th enumber of characters written
# works like this both in write and append mode

#       using with

# with open("another.txt",'r') as f:  #cannot read content when we have declared write mode
#     a=f.read()      #indentation is a must here as we have (:) above
# print(a)
# #       closing is also not needed when used with
# with open("another.txt",'w') as f:  
#     a=f.write("Hey")   #prints 3  
# print(a)