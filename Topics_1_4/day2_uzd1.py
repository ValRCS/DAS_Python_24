import datetime # part of standard Python library

TARGET_AGE = 20
name = input("What is your name ? ")
age = input(f"How old are You {name} ? ")
age = int(age)
end = TARGET_AGE - age
# print(f"Wow {name} in {end} years you will be 💯 years old !")
print(f"Wow {name} in {end} years you will be {TARGET_AGE} years old !")

# now we use datetime we imported at the beginning
current_year = datetime.datetime.now().year
end_year = current_year + end
print(f"It will be in {end_year} !")