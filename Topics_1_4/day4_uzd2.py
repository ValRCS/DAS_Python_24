while True:
    try:
        h = int(input ("Ievadi eglītes augstumu!"))
        # h is int here
        if h <= 0:
           print("Augstumam jābūt pozitīvam skaitlim")
           continue
        # we know we have good input finally
        break
    except ValueError:
        print("Ievadiet lūdzu veselu pozītīvu skaitli")
# so here h is int and over 0

for i in range (1, h + 1):
    print(" " * (h -i) + "*" * (2*i -1))
