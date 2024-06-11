"""
Program: A chocolate factory is packing chocolates into packets.
The chocolate packets here represent array of N number of integer values. 
The task is to find empty packets(0) of chocolates & push to end of conveyor belt
N=8 & arr=[4,5,0,1,9,0,5,0]
"""
a = [4, 0, 5, 0, 1, 9, 0, 0]  # Given list
i = 0  # Initialize index i
j = 0  # Initialize index j
n = 8  # Length of the list

# Iterate through the list
for i in range(len(a)):
    
    # If the element at index i is not equal to 0
    if a[i] != 0:
        # Move the non-zero element to the position indicated by j
        a[j] = a[i]
        # Increment j to move to the next position
        j = j + 1

# After moving all non-zero elements, fill the remaining positions with zeros
while j < n:
    # Set the element at index j to 0
    a[j] = 0
    # Increment j to move to the next position
    j = j + 1

# Print the modified list
for j in a:
    print(j)
# Output : [4,5,1,9,0,0,0,0]
