#  2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem. 

# Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
MIN_SENIORITY = 2
BONUS_RATE = 0.15 # BONUS_PERCENTAGE would be 15 then not 0.15

salary = int(input("What's your salary?"))
seniority = int(input("How many years have you worked for your company?"))
bonus = int(salary * BONUS_RATE * (seniority-MIN_SENIORITY))
# could have use round instead of int - depends on requirements


# Izvadiet bonusu.

if seniority <= MIN_SENIORITY:
     print("better luck next year")
else:
    print("Your bonus this year is ", bonus)