#A file contains the word donkey several times,write a program to replace the word with "##$$##"

# with open("sample.txt") as f:
#     content=f.read()
#     content=content.lower()

# with open("sample.txt",'w') as f1:
#     f1.write(content.replace("donkey","##$$##"))

#Con:converts the whole text to lowercase

# Repeat program for list of such words

words=["mote","kaddu","mc","bc","bkl","mkl","tmkc"]


with open("sample.txt") as f:
    content=f.read()
    content=content.lower()     #can do .lower() in above step itself
for word in words:
    with open("sample.txt",'w') as f1:
        content=content.replace(word,"##$$##")
        f1.write(content)       #f1.write(content.replace(word,"##$$##")) doesn't work here because content needs to be updated after each 
        #censor or else the content would be the one which was read in the start(before loop),so do content=content.replace(word,"##$$##")
        # first to update the content to last itertion change,as write clears everything before writing
        