# What if We Need To Modify a Tuple?
my_tuple = (1, 2, 3)
modified_tuple = my_tuple[:1] + (4,) + my_tuple[2:]
print(modified_tuple)  # Output: (1, 4, 3)

# Iterating over Tuples
my_tuple = (1,2,3,4)
sum = 0
for i in my_tuple:
  sum += i

print("sum is",sum)  # Output: sum is 10

# Using Tuples to Return Multiple Values From a Function
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

rectangle = calculate_rectangle_properties(5, 3)
print(rectangle) # Output: (15, 16)