file = open("learnings.txt", "r")
data = file.read()
print(data)
file.close

# r=reading, w = overwrite, x=newfile, a=open for writing, b=binaryfile open, t=textfile open

file = open("file", "r")
data = file.read()
print(data)
file.close