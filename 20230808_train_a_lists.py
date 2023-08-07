# lists and some it features
# print(f": {list_1}")

list_1 = [1, 3]
print(f"Created list:  {list_1}")

# changing element by index
list_1[0] = 'apple'
list_1[1] = 'tomato'
print(f"Changed list:  {list_1}")

# adding element to the end of list
list_1.append("potato")
print(f"Added new last element: {list_1}")

# inserting new element
list_1.insert(2, 27)
print(f"Inserted 3rd element: {list_1}")

# removing by pop
list_1.pop()
print(f"Popped last element: {list_1}")
popped = list_1.pop(1)
print(f"Popped element with index '1': {list_1}")
print(f"Popped element of a list: {popped}")

print(f"\nFinal list: {list_1}")
