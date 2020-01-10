with open('text.txt', 'r') as file: ## https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    words = file.read().replace('\n', ' ') # replace in text.txt the change line with space
words = words.split() # converts $words variable from string to list of words ## https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
sorted_list = sorted(words, key=len) # put's the words from the sortest to the longet
reversed_list = sorted_list[::-1] # the list is reversed, so it goes from longest to sortest ## https://www.programiz.com/python-programming/methods/list/reverse

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')



#########################################################################


try:
  long_word_0 = reversed_list[0][::-1] # reverse the 1st longest word
  for char in long_word_0:                         ## 
    if char in vowels:                             #### Removes every vowel the word has ## https://stackoverflow.com/questions/21581824/correct-code-to-remove-the-vowels-from-a-string-in-python
      long_word_0 = long_word_0.replace(char, '')  ##
  print("1st longest word in the list is: %s" % (long_word_0,)) # Prints the final result (reversed and with no vowels)

  try:
    long_word_1 = reversed_list[1][::-1]
    for char in long_word_1:
      if char in vowels:
        long_word_1 = long_word_1.replace(char, '')
    print("2nd longest word in the list is: %s" % (long_word_1,))

    try:
      long_word_2 = reversed_list[2][::-1]
      for char in long_word_2:
        if char in vowels:
          long_word_2 = long_word_2.replace(char, '')
      print("2nd longest word in the list is: %s" % (long_word_2,))

      try:
        long_word_3 = reversed_list[3][::-1]
        for char in long_word_3:
          if char in vowels:
            long_word_0 = long_word_3.replace(char, '')
        print("4th longest word in the list is: %s" % (long_word_3,))

        try:
          long_word_4 = reversed_list[4][::-1]
          for char in long_word_4:
            if char in vowels:
              long_word_0 = long_word_4.replace(char, '')
          print("5th longest word in the list is: %s" % (long_word_4,))
        
        
        
        
        except IndexError:
          print("There are no more words")

      except IndexError:
        print("There are no more words")

    except IndexError:
      print("There are no more words")

  except IndexError:
    print("There are no more words")

except IndexError:
  print("Text file is empty! Please put some words :)")



#################################################### Useful sources about this script ####################################################
## https://stackoverflow.com/questions/26132770/python-finding-longest-shortest-words-in-a-list-and-calling-them-in-a-function/44919337
## https://discuss.codecademy.com/t/how-can-i-check-if-an-index-is-valid/377316/4
## https://stackoverflow.com/questions/17015230/are-nested-try-except-blocks-in-python-a-good-programming-practice
##
			
