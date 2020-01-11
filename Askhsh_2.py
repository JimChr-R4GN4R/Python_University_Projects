#with open('text.txt', 'r') as file: ## https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
#words = file.read().replace('\n', ' ') # replace in text.txt the change line with space
#words = words.split() # converts $words variable from string to list of words ## https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words



###########################################################################################

# https://stackoverflow.com/questions/40985203/counting-letter-frequency-in-a-string-python
string=input()
f={}


word_letters_number = 0 # word's letters' number


for i in string:
  f[i]=f.get(i,0)+1
  word_letters_number = word_letters_number + 1 



# https://stackoverflow.com/questions/2932511/letter-count-on-a-string
f_number = int(string.count('f')) # number of f 
c_number = int(string.count('c')) # number of c
k_number = int(string.count('k')) # number of k
r_number = int(string.count('r')) # number of r

total_bad_letters = f_number + c_number + k_number + r_number
total_good_letters = int(word_letters_number - total_bad_letters)

if total_good_letters > total_bad_letters:
  print("Good word")
else:
  print("Bad word! Pepper on your tongue!")

