#1.uzdevums
# Juceklis
# Lietotājs ievada vārdu.
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# Valdis -> Sidlav, pamatigs juceklis vai ne V?
# name = input("Lūdzu ievadiet vārdu:")
# reversed_name = name[::-1].title()
# print(f"{reversed_name}, pamatīgs juceklis vai ne {name[0]}?")

# # Juceklis
name = input("Ieraksti lūdzu savu vārdu ")
cap_name = name.capitalize()
reverse_name = name[::-1].capitalize()
first_letter = name[0].capitalize()
print(f"{cap_name} -> {reverse_name}, pamatīgs juceklis vai ne {first_letter}")

# concatenation version - not complete
# 1.uzdevums
# name = input("Ievadi savu vārdu ")
# reversed_name = name[::-1]
# first_letter_upper = reversed_name[0].upper()
# last_letter_lower = reversed_name[-1:].lower()
# new_name = first_letter_upper + reversed_name[1:-1] + last_letter_lower
# print(f"Jūsu jauns vārds ir {new_name}")
   