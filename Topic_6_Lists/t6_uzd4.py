# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]
while True:
    try:    
        n = int(input("Cik pirmskaitļus gribētos? "))
        break
    except:
        print("Ldzu ievadiet veselu skaitli")

prmsk = [2]
i = 3
# meklējam tikai nepāra skaitļos, vai skaitlis dalās ar kādu no pirmskaitļiem, kas ir masīvā 'prmsk'
while len(prmsk) < n:
    is_prime = True
    for p in prmsk: # no need for sqrt as we are checking only primes so we breek early anyways
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        prmsk.append(i)
    i += 2 # pārbaudam tikai nepāra skaitļus
    # optimization would be to 
    
print(prmsk)