skaitli = []
while True:
    ievade = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if ievade.lower() == 'q': # works on lower and upper case
        break
    try:
        skaitls = float(ievade)
        skaitli.append(skaitls)
        # skaitli.sort() # in place so original order is changed
        # instead we could use sorted(skaitli) which returns a new list
        sorted_skaitli = sorted(skaitli) # this is a new list
        top3 = sorted_skaitli[-3:]
        bottom3 = sorted_skaitli[:3]
        videja_vertiba = sum(sorted_skaitli) / len(sorted_skaitli)
        print("top3 skaitļi:", top3)
        print("bot3 skaitļi:", bottom3)
        print("Vidējā vērtība:", videja_vertiba)
        print("Visi skaitļi:", skaitli)
    except ValueError:
        print("Ievadiet derīgu skaitli!")