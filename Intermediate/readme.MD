# Collection Data Types in Python

## Python Lists

A list in Python is a versatile data structure that can store an ordered collection of items, which can be of different types (integer, float, string, etc.). Lists are mutable, meaning you can change their content without changing their identity.

## Working With List

```python
# An empty list
empty_list = []

# List of integers
int_list = [1, 2, 3, 4, 5]

# List of mixed data types
mixed_list = [1, "Hello", 3.14, True]

# Accessing elements
print(mixed_list[0])  # Output: 1
print(mixed_list[1])  # Output: Hello

mixed_list[1] = "Hi"
print(mixed_list)  # Output: [1, 'Hi', 3.14, True]


# Using append
mixed_list.append("New Element")
print(mixed_list)  # Output: [1, 'Hi', 3.14, True, 'New Element']

# Using insert
mixed_list.insert(1, "Inserted Element")
print(mixed_list)  # Output: [1, 'Inserted Element', 'Hi', 3.14, True, 'New Element']


# Using remove
mixed_list.remove("Hi")
print(mixed_list)  # Output: [1, 'Inserted Element', 3.14, True, 'New Element']

# Using pop
mixed_list.pop(1)
print(mixed_list)  # Output: [1, 3.14, True, 'New Element']

# Using del
del mixed_list[2]
print(mixed_list)  # Output: [1, 3.14, 'New Element']


print(mixed_list[1:3])  # Output: [3.14, 'New Element']
print(mixed_list[:2])   # Output: [1, 3.14]
print(mixed_list[2:])   # Output: ['New Element']
```


## Python Tuple Operations

### Properties of Tuples

1. **Ordered**: Tuples maintain the order of items. The sequence of elements remains consistent.

2. **Immutable**: Tuples cannot be changed after creation. You cannot add, remove, or modify elements.

3. **Heterogeneous**: Tuples can contain elements of different types (integers, floats, strings, etc.).

4. **Hashable**: Tuples can be used as dictionary keys because they are immutable and have a fixed hash value.

5. **Fixed Size**: The size of a tuple is determined at creation and cannot be changed.

6. **Supports Indexing and Slicing**: You can access elements and ranges of elements using indexing and slicing.

7. **Efficient**: Tuples use less memory and are faster than lists when you have a collection of items that do not need to change.

```python
my_tuple = (1, "Hello", 3.14, True)

try:
    my_tuple[1] = "Hi"
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

my_tuple = my_tuple + ("New Element",)
print(my_tuple)  # Output: (1, "Hello", 3.14, True, "New Element")

my_tuple = my_tuple[:1] + my_tuple[2:]
print(my_tuple)  # Output: (1, 3.14, True, "New Element")

print(my_tuple[1:3])  # Output: (3.14, True)
print(my_tuple[:2])   # Output: (1, 3.14)
print(my_tuple[2:])   # Output: (True, "New Element")
```
## Python Dictionaries

A dictionary in Python is an unordered collection of items. Each item is a key-value pair, where each key is associated with a value. Dictionaries are used to store data values like a map, unlike other data types that hold only a single value as an element.

## Key Properties

### Unordered
Dictionaries are unordered collections, meaning items do not have a defined order. When iterating over a dictionary, the order of items may not match the order in which they were added.

```python
# Example demonstrating unordered property
my_dict = {'name': 'Alice', 'age': 25, 'job': 'Engineer'}
print(my_dict)
# Output might not be in the order: {'name': 'Alice', 'age': 25, 'job': 'Engineer'}
