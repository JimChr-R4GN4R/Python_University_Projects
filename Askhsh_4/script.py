string = input("Give a word:")
while string == "":                    ## If input is empty, then ask again.any ## https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained
    string = input("Give a word:")     # 



def   prime_calculator( string ):

  num = ''.join(str(ord(c)) for c in string)
  int_num = int(num)
    
  # If given number is greater than 1 
  if int_num > 1: 
        
    # Iterate from 2 to n / 2  
    for i in range(2, int_num//2): 
          
        # If num is divisible by any number between  
        # 2 and n / 2, it is not prime  
        if (int_num % i) == 0: 
            print(int_num, "is not a prime number") 
            break
    else: 
        print(int_num, "is a prime number") 
    
  else: 
    print(int_num, "is not a prime number") 
    return



prime_calculator(string)
    
    
############################ Useful sources for the script ############################
# https://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
