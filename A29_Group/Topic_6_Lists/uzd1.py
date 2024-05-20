# Vidējā vērtība
 
 
numbers = [] # the ultimate source of truth in this program
while True:
    try:
        raw_input = input("Ievadi skaitli vai q lai izietu:")
        if raw_input.lower().startswith("q"): # so anything starting with q or Q will do
            print("Pietiks!")
            break
        input_number = float(raw_input) 
        # here we know the input is a number
        numbers.append(input_number)
        average = sum(numbers) / len(numbers)
        print(f"Skaitļu vidējais aritmētiskais ir  {average:.2f}") # show only 2 decimal places
        # note .2f is just format it does not change the original number
        # now let's get TOP3 and BOTTOM3 numbers
        sorted_numbers = sorted(numbers) # we sort the numbers into new list
        # on large lists it would be more efficient to sort in place with numbers.sort()
        # numbers are sorted in ascending order by default
        # if we wanted descending we would use sorted(numbers, reverse=True)
        print(f"TOP3 skaitļi ir {sorted_numbers[-3:][::-1]}") # so last 3 elements because we sorted in ascending order
        # [::-1] was used to reverse the slice so we see the biggest numbers first
        print(f"BOTTOM3 skaitļi ir {sorted_numbers[:3]}") # so smallest first
    except ValueError: # for unsuccessful conversion to float
        print("Ievadi citu skaitli")
    # if any other errors were raised we would not catch them and the program would stop
    # so you could add more except blocks for more specific error handling

print(f"Tu ievadīji šos skaitļus {numbers}") # original order