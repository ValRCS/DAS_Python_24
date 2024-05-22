# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30
 
# def add_mult(p1,p2,p3):
#     if p3 >= p2 >= p1 or p3 >= p1 >= p2:
#         return (p1 + p2) * p3
#     elif p2 >= p3 >= p1 or p2 >= p1 >= p3:
#         return (p1 + p3) * p2
#     else:
#         return (p2 + p3) * p1
    

def add_mult(number_1, number_2, number_3, debug=False):
    number_list = [number_1, number_2, number_3]
    if debug:
        print(f"Initial number_list: {number_list}")
    sorted_list = sorted(number_list) # it would have been okay to use number_list.sort() as well
    if debug:
        print(f"Sorted number_list: {sorted_list}")
    # reminder that sorting is ascending by default
    return (sorted_list[0]+sorted_list[1])*sorted_list[2]

print(add_mult(2,5,4)) # 30
# more tests
print(add_mult(2,2,2)) # 8
print(add_mult(1,2,3)) # 9
print(add_mult(1,3,2)) # 9
print(add_mult(3,1,2)) # 9
# let's add 0
print(add_mult(0,0,0)) # 0
print(add_mult(0,0,1)) # 0
print(add_mult(0,1,1)) # 1

# there is third way to solve this problem using max value and no list
# this is neat but maybe not so readable
def add_mult_hacky(number_1, number_2, number_3):
    max_number = max(number_1, number_2, number_3)
    return (number_1 + number_2 + number_3 - max_number) * max_number

print(add_mult_hacky(2,5,4)) # 30

# I would go with the sorted list solution as it is more readable and easier to understand
# now let's debug our function
print(add_mult(2,5,4, debug=True)) # 30
# often this flag is called verbose, either way it is a good practice to have it in your functions