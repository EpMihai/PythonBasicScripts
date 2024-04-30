# Lists are ordered collections of items, and they can contain items of different data types.

# List assignment
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(numbers[0])   # Output: 1
print(fruits[1])    # Output: banana

# Slicing
print(numbers[1:4]) # Output: [2, 3, 4]

# Modifying elements
numbers[0] = 10
print(numbers)      # Output: [10, 2, 3, 4, 5]

# List length
print(len(numbers)) # Output: 5

# Adding elements
numbers.append(6)
print(numbers)      # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
numbers.remove(3)
print(numbers)      # Output: [10, 2, 4, 5, 6]
