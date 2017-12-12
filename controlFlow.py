# Control Flow

a = "Eggs"

if a:
    print("It is true")

h = 42
if h > 50:
    print("Greater than 50")

else:
    print("Less than 50")


# IF-ELSE IF-ELSE

h = 12
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")

# while Looping

c = 5

while c != 0:
    print(c)
    c -=1 # augmented operators

d = 3
while d:
    print(d)
    d -= 1

# How to exit a loop

while True:
    print("Please enter an integer ")
    response = input()
    # Stay in loop until you get a
    # number divisible by 7
    if int(response) % 7 == 0:
        break # exits the loop


