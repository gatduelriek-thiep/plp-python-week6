# Patient 1
for i in range(1, 11): # FIXED: It should stop at 11 since the stopping point is excluded in Python
    print(i)

# Patient 2
n = 3
while n > 0:
    print(n) # FIXED: This will create an infinite loop since the stopping point is not specified
    n = n - 1

# Patient 3
total = 0
for i in range(1, 6):
    total = total + i # FIXED: Total variable that is assigned to 0 should be put up above the loop
print(total)