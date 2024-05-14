# let's start why we need a list or some other sequence type
# imagine we are keeping track of some prices
cena1 = 1.99
cena2 = 2.99
cena3 = 3.50
cena4 = 4.99
# this approach is not very scalable, what if we have 100 prices?
# how about a million or billion?

# Python offers us a list - a sequence type
# list is a collection of items in a particular order
# list properties:
# - ordered
# - mutable - meaning we can change the elements
# - can contain duplicates
# - can contain different types of elements (strings, integers, floats, Booleans, other lists, etc.)
# - can be nested (a list inside a list and so on)
# - dynamic - meaning we can add or remove elements

# again we can store different types of elements in a list
# best practice is to use a descriptive name for the list
# also best to use it for similar items

# creating a list
# we use square brackets [] to define a list or list()

empty_list = [] # we can add to it later
prices = [1.99, 2.99, 3.50, 4.99] # already populated with some values
# very typical to use English plural form for the list name such as prices, names, etc.

# printing everything
print("Empty list", empty_list)
print(f"All prices {prices}")

# how about length of the list
print(f"Length of prices list is {len(prices)}")

# how do I access the first element of the list?
# we use the index of the element which starts at 0
# so to access the first element we use index 0
print(f"First price is {prices[0]}")
# how about the last element?
# we could use the length of the list - 1 but is not Pythonic
# instead we use -1 index which is Pythonic approach
print(f"Last price is {prices[-1]}")

# so lists use dual indexing from 0 to n-1 and from -1 to -n

# mutable - we can change the elements of the list
# let's change the second price
prices[1] = 3.00
print(f"Second price is now {prices[1]}")

# we can calculate sum of all elements if they are numbers
total = sum(prices)
print(f"Total of all prices is {total}")

# we can calculate the average if the prices are all numbers(integers or floats)
# we can use sum and then divide by the length
average = total / len(prices)
print(f"Average price is {average}")

# if we wanted median we could implement it ourselves - that will be in the class exercise
# also we could use statistics module
import statistics
median = statistics.median(prices)
print(f"Median price is {median}") # should be 3.25

# we can add elements to the list
# we can use append method to add an element to the end of the list
# append is the first method that we learn that is a method of a list
# append MODIFIES the list itself
# in Computer Science we call IN-PLACE modification

beers = ["Aldaris", "Cēsu", "Piebalga"]
print(f"Beers {beers}")

beers.append("Tērvete") # modifies the list beers
print(f"Beers {beers}")

# we have a method insert to add an element at a specific index
# insert also modifies the list itself
beers.insert(1, "Bauska") # inserts at index 1 that is second element will be Bauska and Cēsu will be moved to index 2
# insert also modifies the list itself

# alternative so called OUT-OF-PLACE modification meaning we create a new list
# we can use + operator to concatenate two lists
beers = beers + ["Valmiermuiža"] # so overwrites the beers list with new list
# above should be a bit slower than append or even insert
# but it is more flexible
print(f"Beers {beers}")

# let's add Labietis somewhere in the middle
# for that could use insert or we could concatenate two slices of the list

# so we can use slicing to get a part of the list
# first 3 beers
first3 = beers[:3] # slice from 0 to 3 (not including 3)
# last 3 beers
last3 = beers[-3:] # slice from -3 to the end
# Note same syntax as for strings
print(f"First 3 beers {first3} same as {beers[:3]}")
print(f"Last 3 beers {last3}")
# so now let's add Labietis in the middle
beers = first3 + ["Labietis"] + last3 # again we could have used insert instead
# difference is that here we overwrite the beers list
# we could have used an additional list to store the result
print(f"Beers {beers}")

# we could reverse the list and store it in a new list
beers_reversed = beers[::-1] # slice with step -1 and we store in NEW list !
print(f"Beers reversed {beers_reversed}")
# beers reversed is a new list, beers is still the same
print(f"Beers {beers}")
# we can reverse the list in-place
beers.reverse() # modifies the list itself in-place
print(f"Beers reversed {beers}") # original beers list is now reversed
beers.reverse() # modifies the list itself in-place
print(f"Beers reversed {beers}") # original beers list is now reversed back

# important to remember = on a list is NOT a copy of the list by itself
beers_alias = beers # beers_alias is not a copy of beers but an alias , think of it of another sticker/label
# so beers and beers_alias point to the same list
# if we want a copy we need to use copy method
beers_copy = beers.copy() # creates a copy of the list beers, so called shallow copy
# print beers_copy
print(f"Beers COPY {beers_copy}")
# let's get rid of Aldaris in our beers list
beers.remove("Aldaris") # removes the first occurrence of the element
print(f"Beers {beers}")
# alias and copy are still the same
print(f"Beers alias {beers_alias}")
# however copy is different
print(f"Beers copy {beers_copy}")
# same goes for the beers_reversed
print(f"Beers reversed {beers_reversed}")

# slicing however creates a new list
# so theoretically i could copy a list by slicing it
# beers_copy = beers[:] # creates a new list but .copy() is more explicit
# again first 3 beers
first3 = beers[:3] # slice from 0 to 3 (not including 3) this is a copy of the first 3 beers
print(f"First 3 beers {first3}")

# how do we tell if lists are actually the same?
# we have two ways to compare lists
# 1. by identity - are they the same object - so single shopping list
# 2. by equality - do they have the same elements - or two shopping lists with the same items
# let's compare beers and beers_alias
print(f"Beers is beers_alias {beers is beers_alias}") # should be True
# is actually compares memory addresses
# you could have used id(beers) == id(beers_alias) but no need to be so explicit here
# let's compare beers and beers_copy
print(f"Beers is beers_copy {beers is beers_copy}") # should be False
# how about contents
print(f"Beers == beers_copy {beers == beers_copy}") # not True because we took Aldaris out of beers
# print contents
print(f"Beers {beers}")
print(f"Beers copy {beers_copy}")
# let's add Aldaris back to beers to the front
beers.insert(0, "Aldaris")
print(f"Beers {beers}")
# now beers and beers_copy should be equal
print(f"Beers == beers_copy {beers == beers_copy}") # should be True because contents are the same, not the same object

# so is compares by identity, == compares by equality of content in exact order
# compare reversed beers and beers_reversed
print(f"Beers == beers_reversed {beers == beers_reversed}") # should be False because order is different
# compare beers and beers_reversed
print(f"Beers == beers_reversed {beers == beers_reversed[::-1]}") # should be True because content is the same

# so let's add Zoltners to beers
beers.append("Zoltners")
print(f"Beers {beers}")

# let's check existence of a beer in the list
# we can use in operator

# let's check if ZoLtners is in the list
print(f"Zoltners in beers {'Zoltners' in beers}") # should be True
# let's find the index of Zoltners
print(f"Index of Zoltners in beers {beers.index('Zoltners')}") # should be 7
# there is no find method in the list so we will use try except
# so let's look for Carlsberg
try:
    print(f"Index of Carlsberg in beers {beers.index('Carlsberg')}") # going to fail
except ValueError as e:
    print(f"Carlsberg is not in the list of beers {e}")

# we can also count the occurrences of a beer
print(f"Number of Zoltners in beers {beers.count('Zoltners')}") # should be 1
# let's add Labietis to the list again
beers.append("Labietis") # at the end
# let's count Labietis
print(f"Number of Labietis in beers {beers.count('Labietis')}") # should be 2
# Makes sense since we added it twice
print(f"Full list of beers {beers}")

# we now have a situation where the beers are not sorted
# we can sort the list in-place or OUT-OF-PLACE
# let's sort the list out of place creating a new list
beers_sorted = sorted(beers) # creates a new list
# in case of strings they are sorted lexicographically
print(f"Sorted beers {beers_sorted}")
# let's check the original list
print(f"Original beers {beers}")
# so now we will modify the list in-place by using in-place sort
beers.sort() # modifies the list in-place destroys the original order
print(f"Sorted beers {beers}")

# let's add a beer which starts with a Latvian letter
beers.append("Ābols")
# let's sort the list again
beers.sort() # modifies the list in-place
print(f"Sorted beers {beers}")
# we see that Latvian Ā is after English Z in Unicode
# we could add a special custom sort function to sort by Latvian alphabet

# for now I will show how to sort by length
beers.sort(key=len) # modifies the list in-place, so I sead our comparison key is the length of the string
print(f"Sorted beers by length {beers}")

# let's get back to prices
# let's sort them in-place
prices.sort() # modifies the list in-place
print(f"Sorted prices {prices}")
# how about reverse order
prices.sort(reverse=True) # modifies the list in-place
# since prices are already sorted could have just used prices.reverse()
print(f"Reverse sorted prices {prices}")

# let's get back to beers 
# let's add 3 beers at once, Carlsons, Dundulis, and Užavas
beers.append(["Carlsons", "Dundulis", "Užavas"]) # most likely not what we wanted
print(f"Beers {beers}")
# we have created a nested list
# how would I get value of Užavas?
# we would use double indexing
print(f"Užavas {beers[-1][-1]}") # should be Užavas, last item in the last list
# how about Dundulis?
print(f"Dundulis {beers[-1][-2]}") # should be Dundulis, second to last item in the last list
# same as beers[-1][1] but I prefer to use negative indexing
# let's remove our last element but let's use pop method

# pop removes the last element of the list and returns it so you can save it if you want
# some languages destroy the element, Python does not
last_beers = beers.pop() # modifies the list in-place so last element is removed and saved in last_beers
print(f"Last beers {last_beers}")
print(f"Beers {beers}")
# if we want to have flat list we can use extend method
beers.extend(["Super Bock", "Duff Beer", "Užavas"]) # modifies the list in-place so adds the elements to the end
print(f"Beers {beers}")

# let's make a copy before we clear everything
beers_copy = beers.copy() # creates a copy of the list beers
# let's clear the list
beers.clear() # modifies the list in-place so removes all elements 
print(f"Beers {beers} :(")
# let's get our beers back by using copy
# i can not pop from empty list
try:
    last_beers = beers.pop() # going to fail
except IndexError as e: # i can use as e to get the exception object
    print(f"Can not pop from empty list {e}")

# we also get IndexError if we try to access an element that does not exist
try:
    print(f"First beer {beers[0]}") # going to fail since I have NO beers at all
except IndexError as e:
    print(f"Can not access first beer {e}")

# however slicing does not fail
print(f"First 3 beers {beers[:3]}") # should be empty list
# so we can not pop or access an element that does not exist
# but we can slice an empty list
print("Let's get our beers back")
beers = beers_copy.copy() # restores the beers list from copy
print(f"Beers {beers}")
# let's get last 5000 beers this is a legal slice
print(f"Last 5000 beers {beers[-5000:]}") # should be the same as beers

# so now let's do loops
# let's print all beers one by one
for beer in beers: # so very similar to strings
    print(beer)

# if i need index I should use enumerate
# range is not needed since we have a list
for i, beer in enumerate(beers,start = 1): # start is optional and defaults to 0
    print(f"Beer No.{i}. {beer}")

# let's add Lowenbrau to the list
beers.append("Lowenbrau")
# all beers just normal print
print(beers)

# let's get all beers that start with L
# we could use a for loop
beers_with_l = []
for beer in beers:
    # if beer[0] == "L": # better use startswith method
    if beer.startswith("L"):
        beers_with_l.append(beer) # adds a copy of the beer to the list
print(beers_with_l)
