import re
words = text.readlines()
print(words)
words = words.split()
sortedwords = sorted(words, key=len)
print("The longest word in the list is: %s." % (sortedwords[-1],))
print("The longest word in the list is: %s." % (sortedwords[-2],))
print("The longest word in the list is: %s." % (sortedwords[-3],))
print("The longest word in the list is: %s." % (sortedwords[-4],))
print("The longest word in the list is: %s." % (sortedwords[-5],))
# https://stackoverflow.com/questions/26132770/python-finding-longest-shortest-words-in-a-list-and-calling-them-in-a-function/44919337
