
f={}

def freq(str): 
  
    # break the string into list of words  
    str = str.split()          
    str2 = [] 
  
    # loop till string values present in list str 
    for i in str:              
  
        # checking for the duplicacy 
        if i not in str2: 
  
            # insert value in str2 
            str2.append(i)  
              
    for i in range(0, len(str2)): 
  
        # count the frequency of each word(present  
        # in str2) in str and print 
        word_letters_number = 0
        for j in str2[i]:
          f[i]=f.get(i,0)+1
          word_letters_number = word_letters_number + 1
          f_number = int(str2[i].count('f')) # number of f 
          c_number = int(str2[i].count('c')) # number of c
          k_number = int(str2[i].count('k')) # number of k
          r_number = int(str2[i].count('r')) # number of r
          total_bad_letters = f_number + c_number + k_number + r_number
          total_good_letters = int(word_letters_number - total_bad_letters)

        if total_good_letters > total_bad_letters:
          print(str2[i], 'is : Good word')  
        else:
          print(str2[i], 'is : Bad word! Pepper on your tongue!')   
  
def main(): 
    with open('text.txt', 'r') as myfile:
      str=myfile.read().replace('\n', ' ',)
    freq(str)                     
  
if __name__=="__main__": 
    main()             # call main function 



########################### Useful sources for the script ###########################
# https://www.geeksforgeeks.org/find-frequency-of-each-word-in-a-string-in-python/
# https://stackoverflow.com/questions/2932511/letter-count-on-a-string
# Ashsh_1's script
