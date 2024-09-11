from unit1lesson2 import *
smallest_number = number_list[0]

if number_list[1] < smallest_number:
    smallest_number = number_list[1]
for x in number_list:
    if x < smallest_number:
     smallest_number = x
     
print(smallest_number)
print(" The smallest number in this list is: " + str(smallest_number) )

#OMG finaaaally. I kept getting a syntax error about line one that I could not understand. I eneded up resetting everything and it worked.

smallest_number > 500
print (smallest_number)

#ok did not work

for x in number_list:
   if x > 500:
      smallest_number = x
print(smallest_number)

#this neither

smallest_number_over_500 = None  # Starting None cus no valid number yet

for x in number_list:
    if x > 500:  # We only care about numbers greater than 500
        if smallest_number_over_500 is None or x < smallest_number_over_500:  # Find the smallest of them
            smallest_number_over_500 = x

if smallest_number_over_500 is not None:
    print("The smallest number over 500 is:", smallest_number_over_500)
else:
    print("There is no number over 500 in the list.")

# We start by saying the smallest even number is 'infinity' (a super big number)
smallest_even = float('inf')

# We look at each number in the list
for x in number_list:
    # Check if the number is even (no leftovers when divided by 2)
    if x % 2 == 0:
        # If this number is smaller than the one we remembered, remember this new one
        if x < smallest_even:
            smallest_even = x

# Now, check if we ever found a smaller even number
if smallest_even == float('inf'):
    print("There is no even number in the list.")
else:
    print("The smallest even number in the list is:", smallest_even)
#Rae, I had Chat explain these to me like I am five and i am ctually now understanding wth is going on lol

last_word = word_list[0]

# Look through all the words in the list
for word in word_list:
    # If this word comes after the word we remembered, remember this new word
    if word > last_word:
        last_word = word

# Print out the word that comes last alphabetically
print("The word that comes last alphabetically is:", last_word)

#im gunna try this last one on my own and leave what ever answer it gives me 

#longest_word = 0
#if len(longest_word) < 0 + 1
#len(longest_word) = word

 #I knew this wasn't right before I ran but at least I understand why now .. I just dont know that I know the variables to explain..
 #The longest word is hypothetically word one until we find a word longer as we go down the list
 #buuuut, okay let me try something

for longest_word in word_list:
    longest_word = len(longest_word)
if len(longest_word + 1) < longest_word:
    print("The longest word in the word list is:", longest_word)

#i haven't run this yet but im feeling very confident lmaao

##nope lol, but an A+ cus i feel more knowledgeable