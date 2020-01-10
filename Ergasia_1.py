words = "Hello I like lookies cookies1"
words = words.split() # takes $words' input and puts it's words in a list ## https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
sorted_list = sorted(words, key=len) # put's the words from the sortest to the longet
reversed_list = sorted_list[::-1] # the list is reversed, so it goes from longest to sortest ## https://www.programiz.com/python-programming/methods/list/reverse
print("The longest word in the list is: %s." % (sortedwords[0],)) # 1st longest word
print("The longest word in the list is: %s." % (sortedwords[1],)) # 2nd longest word
print("The longest word in the list is: %s." % (sortedwords[2],)) # 3rd longest word
print("The longest word in the list is: %s." % (sortedwords[3],)) # 4th longest word
print("The longest word in the list is: %s." % (sortedwords[4],)) # 5th longest word
## https://stackoverflow.com/questions/26132770/python-finding-longest-shortest-words-in-a-list-and-calling-them-in-a-function/44919337
