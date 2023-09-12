############## File Handling ############
# Write inside the file
file = open("Hello.txt","w")
# a - append | r - read | w - write
file.write("Hello CK")
# We need to close the file 
file.close()

# Append information inside the file.
file = open("Hello.txt","a")
file.write("\nCK")
file.close()

# Read content inside the file.
file = open("Hello.txt","r")
print(file.read())
file.close()

# Store every line in a container within the file content
file = open("Hello.txt","r")
numbers = file.readlines()
for items in numbers:
    print(items.strip())
file.close()

# Store every line in a container within the file content, then add every numbers
file = open("Hello.txt","r")
numbers = file.readlines()
sum = 0
for items in numbers:
    sum += int(items.strip())
file.close()
print(sum)




