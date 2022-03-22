import os

with open("userinput/data1.txt", "r") as f:
    f_contents = f.read()
    os.system(f_contents)



