with open('text.txt', 'r') as file: ## https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    words = file.read().replace('\n', ' ') # replace in text.txt the change line with space
words = words.split() # converts $words variable from string to list of words ## https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
sorted_list = sorted(words, key=len) # put's the words from the sortest to the longet
reversed_list = sorted_list[::-1] # the list is reversed, so it goes from longest to sortest ## https://www.programiz.com/python-programming/methods/list/reverse


try:

   print("1st longest word in the list is: %s" % (reversed_list[0],))

   try:

     print("2nd longest word in the list is: %s" % (reversed_list[1],))

     try:

       print("3rd longest word in the list is: %s" % (reversed_list[2],))


       try:

         print("4th longest word in the list is: %s" % (reversed_list[3],))


         try:
           print("5th longest word in the list is: %s" % (reversed_list[4],))
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

## https://stackoverflow.com/questions/26132770/python-finding-longest-shortest-words-in-a-list-and-calling-them-in-a-function/44919337
## https://discuss.codecademy.com/t/how-can-i-check-if-an-index-is-valid/377316/4
