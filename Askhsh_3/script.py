prices = {
    "banana": 100,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!

def compute_bill(food):
    total = 0
    for item in food:
        item = shopping_list(prices[key])
        total += item
    return total

###################

shopping_list = [] 
maxLengthList = 6
while len(shopping_list) < maxLengthList:
    item = input("Enter your Item to the List: ")
    shopping_list.append(item)
    print(shopping_list)
print("That's your Shopping List")
print(shopping_list)

##################



cost = sum([ prices[s] for s in shopping_list ])
foros = cost * 24 / 100

sum_cost = foros + cost

print(sum_cost)



###########################
#https://stackoverflow.com/questions/29189978/computing-shopping-list-total-using-dictionaries
#https://stackoverflow.com/questions/21043387/how-do-you-add-input-from-user-into-list-in-python#21043528
