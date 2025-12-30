# Taking input
str = input("Enter a string: ")
starting_index = int(input("Enter the starting index: "))
ending_index = int(input("Enter the ending index: "))
step_value = int(input("Enter the step value: "))

# Error handling for step value
if step_value == 0:
    print("Step value cannot be zero. Please enter a non-zero integer.")
    step_value = int(input("Enter the step value: "))

# Slicing the string
sliced_string = str[starting_index:ending_index:step_value]

print("The sliced string is:", sliced_string)


