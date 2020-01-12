###### Available items with their costs ######
prices = {
    "banana": 100,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
##############################################


def compute_bill(food):
    total = 0
    for item in food:
        item = shopping_list(prices[key])
        total += item
    return total

##################### Shoping list input ############################

shopping_list = [] 
while len(shopping_list) < 100: # maximum items you can add are 100
    item = input("Enter your Item to the List: ")
    if item == '': # If finished and press enter, then stop the loop
      break
    shopping_list.append(item)
#####################################################################



cost = sum([ prices[s] for s in shopping_list ])
foros = cost * 24 / 100

sum_cost = foros + cost

print(sum_cost, "€")



###########################
#https://stackoverflow.com/questions/29189978/computing-shopping-list-total-using-dictionaries
#https://stackoverflow.com/questions/21043387/how-do-you-add-input-from-user-into-list-in-python#21043528
