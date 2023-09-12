############## File Handling ############
file = open("Hello.txt","r")
# a - append | r - read | w - write
print(file.read())
# We need to close the file 
file.close()
