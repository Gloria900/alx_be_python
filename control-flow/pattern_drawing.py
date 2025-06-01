# # Step 1: Ask the user to enter the size of the pattern
# size = int(input("Enter the size of the pattern: "))
#
# # Step 2: Initialize row counter
# row = 1
#
# # Step 3: Use a while loop to control the rows
# while row <= size:
#     # Step 4: Use a for loop inside the while to print stars in a row
#     for column in range(size):
#         print("*", end="")  # Print star without moving to next line
#     print()  # Step 5: Move to the next line after each row
#     row += 1  # Go to the next row
pattern_size = int(input("Enter the size of the pattern:"))
rows = 1
while rows <= pattern_size:
    for column in range(pattern_size):
        print("*", end="")
    print()
    rows +=1