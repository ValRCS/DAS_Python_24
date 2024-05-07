START = 1
END = 100  # Mainīgais, kas norāda, līdz kuram skaitlim izdrukāt virknīti
FIZZ_NUM = 5 # original was 3
BUZZ_NUM = 7 # original was 5
# we could even adjust fizz and buzz messages / strings here as variables

for i in range(START, END+1):
    end = ", " # default for our needs
    if i == END:
        end = " 🍺\n" # so happens this is the real default but could be anything
    # previous 3 rows could have been if else which is completely fine
    
    if i % FIZZ_NUM == 0 and i % BUZZ_NUM == 0: # būtiski lai šī būtu pirmā pārbaude
        print("FizzBuzz", end=end) # default end for print is "\n"
    elif i % FIZZ_NUM == 0:
        print("Fizz", end=end)
    elif i % BUZZ_NUM == 0:
        print("Buzz", end=end)
    else:
        print(i, end=end)