words = "Hello I like lookies cookies1"
words = words.split()
sortedwords = sorted(words, key=len)
print("The longest word in the list is: %s." % (sortedwords[-1],))
print("The longest word in the list is: %s." % (sortedwords[-2],))
print("The longest word in the list is: %s." % (sortedwords[-3],))
print("The longest word in the list is: %s." % (sortedwords[-4],))
print("The longest word in the list is: %s." % (sortedwords[-5],))
