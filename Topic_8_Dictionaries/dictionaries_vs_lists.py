# common question is why should I use dictionaries when I can use lists?
# again with dictionaries, you can use keys to access values, which is much more efficient than using unknown indexes
# let's say I want to store foods and their prices
# I can use a list of lists
food_prices_list = [['apple', 0.99], ['banana', 0.59], ['orange', 0.79]]
# how would I find price for banana?
# I would have to iterate over the list and check if the first element is 'banana'
needle = 'banana'
for food in food_prices_list: # linear process so if I have millions of items, it will take a while
    if food[0] == needle:
        print(f"Price of {needle} is {food[1]}")
        break

# instead let's do this with dictionaries
food_prices_dict = {'apple': 0.99, 'banana': 0.59, 'orange': 0.79}
# now i simply can access the price of banana
print(f"Price of {needle} is {food_prices_dict[needle]}") # food_prices['banana'] would also work, and equally fast