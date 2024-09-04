
# Print a blank line
print("\n")

# Ask the user for a filename
filename = input("Please enter the name of a file in this directory: ")

# Open that file
file = open(filename)

print("Name is: " + file.readline())
print("Title is: " + file.readline())
print("Phone number is: " + file.readline())
print("Address is: " + file.readline())
    file = open(filename)
FileNotFoundError: [Errno 2] No such file or directory: ' test.py'
as-MacBook-Air:unit-1 a.naniwilliams$ /usr/bin/python3 /Users/a.naniwilliams/fa-24-ITC/unit-1/lesson-1/business_card_read.py


Please enter the name of a file in this directory: business_card_create.py
Traceback (most recent call last):
  File "/Users/a.naniwilliams/fa-24-ITC/unit-1/lesson-1/business_card_read.py", line 9, in <module>
    file = open(filename)
FileNotFoundError: [Errno 2] No such file or directory: 'business_card_create.py'
as-MacBook-Air:unit-1 a.naniwilliams$ 