f1=open("example.txt","w")  # can give the file name or path
f1.write("welcome to file handling concepts \n")
f1.write("to create new line use \n")
for i in range(1,4):
    print(f1.readline())
f1.close()

f2=open("./file_handling/example.txt","r")

for i in range(1,4):
    print(f2.readlines())

f2.close()

f3 = open("./file_handling/example.txt", "r") # to read upto certain characters then we use the path in open
print (f3.read(5))

# to append the data
file = open("./file_handling/example.txt", "a")
file.write("append mode add this line")
file.close()




