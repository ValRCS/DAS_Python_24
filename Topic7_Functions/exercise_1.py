# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30

def add_mult(a, b, c):
    nums = [a, b, c] # create a new list from arguments
    nums.sort() # ascending order
    return (nums[0] + nums[1]) * nums[2] # nums will be destroyed after function ends

# alternative solution without sorting using min and max
# we want the two smallest numbers to add and then multiply by the largest number
# def add_mult(a, b, c):
#     return (a + b + c - max(a, b, c)) * max(a, b, c)
# so we added all 3 and took away the largest number and then multiplied by the largest number

# now a version where a list is passed instead of arguments
def add_mult_list(numbers):
    numbers = sorted(numbers)
    # assumption that we have at least 2 numbers
    return (numbers[0] + numbers[1]) * numbers[-1] # so now it works on possibly more than 3 numbers


 
# Piemērs:
result = add_mult(2, 5, 4)
print(result)  # Atgriezīs 30
number_list = [2, 5, 4]
result = add_mult_list(number_list)
print(result)  # Atgriezīs 30