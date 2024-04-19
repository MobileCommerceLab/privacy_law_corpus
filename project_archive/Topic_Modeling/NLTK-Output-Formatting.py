import re

regex = re.compile('[^a-zA-Z]')

arr = []

with open("6Topics-9Passes-update_every2.txt","r") as file:  ## Change File path. This must be the output of the NLT Code
    lines = file.readlines()
    for line in lines:
        line = line.lower()
        line = str(line).split()
        temp = regex.sub(' ', str(line))
        arr.append(temp)
         
file = open("Clean-Latest-6Topics-9Passes-update_every2.txt","w") ## Change File path to write the formatted output into
for i in arr:
     a = i.split()        
     file.write(str(a)+"\n")
file.close()
