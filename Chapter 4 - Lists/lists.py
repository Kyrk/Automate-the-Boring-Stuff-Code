#!/usr/bin/env python3
"""Notes/tidbits from chapter"""
spam = ['cat', 'bat', 'rat', 'elephant']

# 4th element in list
print("EX 1")
spam1 = spam[3]
print(spam)

# List containing other list values
print("\nEX 2")
spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam2[0])
print(spam2[0][1])
print(spam2[1][4])

# Negative indexes
print("\nEX 3")
print('The {} is afraid of the {}'.format(spam[-1], spam[-3]))

# Slices
print("\nEX 4")
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

# Slice shortcuts
print("\nEX 5")
print(spam[:2])
print(spam[1:])
print(spam[:])

# List length
print("\nEX 6")
print(len(spam))

# Change value in list with indexes
print("\nEX 7")
spam3 = ['cat', 'bat', 'rat', 'elephant']
spam3[1] = 'aardvark'
print(spam3)
spam3[2] = spam3[1]
print(spam3)
spam3[-1] = 12345
print(spam3)

# List concatenation/replication
print("\nEX 8")
nums = [1, 2, 3]
letters = ['A', 'B', 'C']
print(nums + letters)
print(letters * 3)
both = nums
both += letters
print(both)


# for loops with lists
print("\nEX 9")
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index {} in supplies is: {}'.format(str(i), supplies[i]))

# in and not in
print("\nEX 10")
print('howdy' in ['hello', 'hi', 'howdy'])
print('cat' in spam)
print('bat' not in spam)
print('cat' not in spam)

# Multiple assignment/tuple unpacking
print("\nEX 11")
cat = ['fat', 'gray', 'loud']
# This...
size = cat[0]
color = cat[1]
disposition = cat[2]
# ...is the same as
size, color, disposition = cat
print('{} {} {}'.format(size, color, disposition))

# enumerate
print("\nEX 12")
for index, item in enumerate(supplies):
    print('Index {} in supplies is {}'.format(str(index), item))

# random.choice() and random.shuffle() with lists
print("\nEX 13")
import random # module required
pets = ['Dog', 'Cat', 'Moose']
for i in range(3):
    print(random.choice(pets))
people = ['Alice', 'Bob', 'Carol', 'David']
for i in range(3):
    random.shuffle(people)
    print(people)

# Find value in list
print("\nEX 14")
print(spam)
print(spam.index('cat'))
print(spam.index('elephant'))

# Add values to lists
print("\nEX 15")
spamad = spam
spamad.append('moose')
print(spamad)
spamad.insert(1, 'chicken')
print(spamad)

# Delete and remove values
print("\nEX 16")
spamd = ['cat', 'bat', 'rat', 'elephant']
del spamd[2]
print(spamd)
del spamd[2]
print(spamd)

spamrem = ['cat', 'bat', 'rat', 'elephant']
spamrem.remove('bat')
print(spamrem)
spamrem *= 2
spamrem.remove('elephant')
print(spamrem) # only first instance is removed
# del = index, remove = value

# Sort values
print('\nEX 17')
span = [2, 5, 3.14, 1, -7]
print('NOT SORTED: ' + str(span))
span.sort()
print('SORTED: ' + str(span))
print('NOT SORTED: ' + str(spam))
spam.sort()
print('SORTED: ' + str(spam))
spam.sort(reverse=True)
print('REVERSED: ' + str(spam))
