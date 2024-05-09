#Lietotājs ievada vārdu.
#Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
#Valdis -> Sidlav, pamatigs juceklis vai ne V?
#

name = input("Lūdzu ievadiet vārdu: ")
reverse_name = name[::-1]
print(reverse_name.lower().title() + ", pamatīgs juceklis vai ne", name[0] + "?")
# same with f-strings
print(f"{reverse_name.title()}, pamatīgs juceklis vai ne {name[0]}?")
# without any extra variables
print(f"{name[::-1].title()}, pamatīgs juceklis vai ne {name[0]}?")