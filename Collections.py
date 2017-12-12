# Collections
# Strings: str
# Bytes: bytes
# Arrays: list
# Dictionary: dict

# 1) Strings: Immutable sequence of unicode codepoints
# Single and double quotes

h = 'This is a string'

print(h)

h = "This is a string's double quotes"

print(h)

# Multi-line strings: triple double or single quotes

h = """This is a
long multi line
string"""

print(h)

m = "This is \nmulti\nline"
print(m)

m = "This\\ is \nmulti\nline"

print(m)

# Raw strings

path = r'C:\User\Documents\Books'
print(path)

# String as sequences
s = "parrot"
print(s[0])
print(s[4])

# Use the type() function to get the object's type
print(type(s))

#2) Bytes: similar to strings, but instead a sequence
# of unicode points is a sequence of bytes.
# use for raw binary data, fixed-width, ASCII
bt = b'data'
print(bt)



# Encode data: utf-8
l = "Visitamos el zooló"
print(l)
data = l.encode("utf-8")
print(data)
# now decode it
s = data.decode("utf-8")
print(s)

# 3) Arrays: A list of mutable objects
# Replace, remove, or append elements
# Delimited by [], and items are
# separated by commas

l = [1, 2, 3]
print(l)
print(type(l))
a = ["apple", "orange", "pear"]
print(a[1])

# can have a mix of data types
b = ["Waldo", 2, 4.5]
print(b)
print(type(b[2]))

ll = ["apple", "john", [1, 2, 3]]
print(ll[2][1])

# Add members
b.append("giraffe")
print(b)

# list constructor: list()

m = list("Characters")
print(m)

# insert into a list and specify the position
b.insert(2, "Goat")
print(b)

# Dictionaries: Mutable mapping of keys to values
# Values are in no particular order
# {k1: v1, k2: v2}

d = {"alice":"810-789-4562", "Pedro":"956-1232-7845"}
print(type(d))
print(d)

# Access a member
print(d["alice"])
# Update the members value
d["alice"] = '801-789-4562'
print(d)
# If value exists it is updated
# If value does not exist it will add it
d['maria'] = '123-459-7845'
print(d)

# For loops: visit each item in an iterable series
cities = ["London", "Madrid", "Paris", "Ogden"]
for city in cities:
    print(city)

# Access members of dictionary, a for loop gets
# the key value.
for i in d:
    print(i,"=>",d[i])


