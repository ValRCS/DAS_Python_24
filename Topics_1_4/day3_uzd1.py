# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"
COLD_TEMP = 35
FEVER_TEMP = 37

temperature = float(input("What's your temperature?"))
# 
# if temperature < 35:
#      print("nav par aukstu")
# elif temperature > 37:
#     print("iespējams drudzis")
# else: # 35 <= temperature <= 37
#     print("viss kārtībā")

if temperature < COLD_TEMP: # compared first
    print("nav par aukstu")
# elif COLD_TEMP <= temperature <= FEVER_TEMP: # ok but not required
elif temperature <= FEVER_TEMP: # means COLD_TEMP <= temperature <= FEVER_TEMP
    print("škiet viss kārtībā")
else: # so over FEVER_TEMP
    print("iespējams drudzis")