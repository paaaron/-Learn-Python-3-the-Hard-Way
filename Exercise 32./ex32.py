the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'penies', 2, 'dimes', 3, 'quartes']

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")
# same as above

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed list too
# notice we have to use {} since we don't know what's in it

for i in change:
    print(f"I got {i}")

# we also build list, first start with a empty one
elements = []
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that list understand
    elements.append(i)

# now we can print them out too

for i in elements:
    print(f"Elements was: {i}")