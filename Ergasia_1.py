words = "Hello I like lookies cookies1"
words = words.split() # takes $words' input and puts it's words in a list 
sortedwords = sorted(words, key=len) # puts the words from the shortest to the longest
print("The longest word in the list is: %s." % (sortedwords[-1],)) # 1st longest word
print("The longest word in the list is: %s." % (sortedwords[-2],)) # 2nd longest word
print("The longest word in the list is: %s." % (sortedwords[-3],)) # 3rd longest word
print("The longest word in the list is: %s." % (sortedwords[-4],)) # 4th longest word
print("The longest word in the list is: %s." % (sortedwords[-5],)) # 5th longest word
# https://stackoverflow.com/questions/26132770/python-finding-longest-shortest-words-in-a-list-and-calling-them-in-a-function/44919337
