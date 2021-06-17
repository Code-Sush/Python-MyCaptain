print("This program gets the file name from the user and prints the extension of it")
finame=input("Input the file name with extension : ")
for i in range(0,len(finame)):
 if finame[i] == ".":
  exname=finame[i:len(finame)]

print("Extension: ",exname)
