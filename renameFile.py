#Write a program to rename a file to "renamed_by_python.txt"

import os 

oldName="removingfile.txt"
newName="newname.txt"

# Check if the original file exists
if os.path.exists(oldName):
    os.rename(oldName,newName)
    print(f"renamed {oldName} to {newName}")
else:
    print(f"{oldName} doesn't exist")

#Harry did it by copying content and then removing the old file using os module (os.remove(OldName))

#If you want to mention the path
# import os
# old_file = os.path.join("directory", "a.txt")
# new_file = os.path.join("directory", "b.kml")
# os.rename(old_file, new_file)

#path.join concatenates different parts of file path into a single path string