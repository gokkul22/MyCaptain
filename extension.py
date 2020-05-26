file = input("Type a file:")
f = file.split(".")                                                  #to spilt the string into two as before and after the dot
print ("The extension of the file is : " + str(f[-1]))               #to print the string after dot


Output:

Type a file:hello.c
The extension of the file is : c
