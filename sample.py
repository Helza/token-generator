# Simple Python script

# Prompt user for name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# Greet the user
print(f"Hello, {name}! You are {age} years old.")

# Check if the user is an adult
if int(age) >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
