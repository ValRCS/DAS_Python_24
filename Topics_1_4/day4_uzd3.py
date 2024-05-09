# Thanks to Agris for initial version of the code
# import math

i=2
pirm_sk=True

#sk=int(input("ievadiet skaitli: "))
# let's make sure we get positive integer
while True:
    try:
        sk = int(input("Ievadiet lūdzu veselu pozītīvu skaitli: "))
        if sk <= 0:
            print("Skaitlim jābūt pozitīvam skaitlim")
            continue
        break
    except ValueError:
        print("Ievadiet lūdzu veselu pozītīvu skaitli")


# optimized version that checks only up to sqrt(sk)
# because if the divisor is over sqrt(sk) then the other divisor is less than sqrt(sk)
while i <= int(sk**0.5):
    if sk%i == 0:
        print("Nav pirmskaitlis!")
        print(f"{i} * {sk//i} = {sk}")
        pirm_sk=False
        break
    i+=1

if pirm_sk==True:
    print(f"Ievadītais skaitlis {sk} ir pirmskaitlis!")
else:
    print(f"Ievadītais skaitlis {sk} NAV pirmskaitlis!")