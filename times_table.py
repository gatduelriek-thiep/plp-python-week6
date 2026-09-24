# Ask the user to input his / her favorite number
user = int(input("What is your favorite number? "))

# Iterate using a for loop
for i in range(1, 11):
    print(f"{user} x {i} = {user * i}")

print()
print("This is the end of the for loop")
