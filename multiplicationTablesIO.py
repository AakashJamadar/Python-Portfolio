#write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Plcce the files in a folder for a 13 yo

import os

folder_name="Multiplication_tables"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


for i in range(2,21):
    file_path=os.path.join(folder_name,f"multiplication_tables_of_{i}.txt")
    with open(file_path,'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}")
            if j!=10:
                f.write("\n")