###### Available items with their costs ######
prices = {                                  ##
    "banana": 1.28,
    "apple": 2.3,
    "orange": 1.5,
    "pear": 3
}                                           ##
##############################################
cost = 0
foros = 0

def compute_bill(food):
    total = 0
    for item in food:
        item = shopping_list(prices[key])
        total += item
    return total



###################################### Cost calculate function
                                  ##
def ComputeCost(cost):
  foros = cost * 24 / 100

  sum_cost = foros + cost
  return sum_cost
                                  ##
####################################

##################### Shoping list input #################################################################
                                                                                                        ##
shopping_list = []                                                                                      ##
while len(shopping_list) != "": # Add until give no input
    item = input("Enter your Item to the List (one per time): ")

    if item == '': # If finished then press enter, then stop the loop
        break
    elif item == 'help': # Show menu
        print(prices)
    else:
        try: # Checks if input exists in the list
          shopping_list.append(item)
          cost = sum([ prices[s] for s in shopping_list ])
          ComputeCost(cost)
        except KeyError:
          print("Item does not exist in the list")
          shopping_list = shopping_list[:-1] # if input is not exist,then delete it from $shopping_list
                                                                                                        ##
                                                                                                        ##
##########################################################################################################



print(round(ComputeCost(cost), 2), "€")



########################### Useful sources for the script ###########################
#https://stackoverflow.com/questions/29189978/computing-shopping-list-total-using-dictionaries
#https://stackoverflow.com/questions/21043387/how-do-you-add-input-from-user-into-list-in-python#21043528
#https://stackoverflow.com/questions/18169965/how-to-delete-last-item-in-list#18170372
#https://stackoverflow.com/questions/3914725/how-to-turn-a-float-number-like-293-4662543-into-293-47-in-python
