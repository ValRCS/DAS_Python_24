# 2.Kubu tabula
while True:
    try:
        list_start = int(input("Lūdzu ievadiet vesela tipa sākuma skaitli!"))
        list_end = int(input("Lūdzu ievadiet vesela tipa beigu skaitli!"))
        break
    except ValueError:
        print("Ievadiet veselu skaitli gan sākumam gan beigām!")
# list_start = int(input("Lūdzu ievadiet vesela tipa sākuma skaitli!"))
# list_end = int(input("Lūdzu ievadiet vesela tipa beigu skaitli!"))
# if we wanted to support going down we need to add a step
if list_start <= list_end: # so if same we have a list of 1 number
    step = 1
else: # list_start > list_end:
    step = -1

numbers = list(range(list_start,list_end+step, step)) # we need to use step +1 to include the end number
print(numbers)
cubes = []
for number in numbers:
    num_cube = (number ** 3)
    print(f"{number} kubā ir {num_cube}")
    cubes.append(num_cube)
print(f"Visi kubi rindiņā: {cubes}.")