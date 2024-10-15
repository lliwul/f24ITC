import string
document = {}
with open('cogitoergosum.txt', 'r') as file:
# file = 'cogitoergosum.txt' 
    for line in file:
     words = line.split()
     for word in words:
            if word in document:
                #if the word is in the document the value of that word equals 1
                document[word] += 1
            else:
                #establishes frequency for words newly encountered
                document[word] = 1
    # for how, many in document.items():
    #     print(how, many)

    #wrote all on my own, with direction and help of google. BUT. it is only returning the last line of my file.
    #going to see if chat can find the error i am not seeing.
    #wait! im going to review unit 1 first.
    # Okay chat helped: "for word" needed to be in "for line"

    #okay now i want it to sort in numerical order
sorted_document = sorted(document.items(), key=lambda x: x[1], reverse=True)

# Now print the words and their frequencies in numerical order
for how, many in sorted_document:
    print(how, many)

# top words: 
# if 7
# The 6
# past 6
# In 6
# being 6
# simply 6
# do 6
# Still 6
# As 6
# no 6
# It 5
# first 5
# own 5
# never 5
# how 5