######### Conditional Loops #############
# age = 19

# if age >20:
#     print("You are older than 20.")
    
# else:
#     print("You are younger than 20")

# While loop
# num = 0

# while num < 10:
#     print(num)
#     num = num + 1
# -> This will result to infinite printing

# For loops
# for num in range(10):
#     print(num)

# Guessing game
secret_number = 4

guess = int(input("Enter your guess: "))

while guess != secret_number:
    if guess < secret_number:
        print("Guess too low")
    else:
        print("Guess too high")
        
print("Congratulations you have won!")
