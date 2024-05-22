# 4. Pirmskaitļi 
number_of_primes = int(input("How many prime number do you want to see? "))
primes = [2]
num = primes[0] + 1
while len(primes) <= number_of_primes:
    isprime = True
    for i in primes: # here we could check up to sqrt(num) but this is simpler
        if num % i:
            continue
        else:
            isprime = False
            break
    if isprime:
        primes.append(num)
    num += 2
print(primes)