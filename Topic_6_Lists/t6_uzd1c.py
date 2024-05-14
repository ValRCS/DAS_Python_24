skaitli = []
while True:
    ievade = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if ievade.lower() == 'q': # works on lower and upper case
        break
    try:
        skaitls = float(ievade)
        skaitli.append(skaitls)
        skaitli.sort() # in place
        top3 = skaitli[-3:]
        bottom3 = skaitli[:3]
        videja_vertiba = sum(skaitli) / len(skaitli)
        print("top3 skaitļi:", top3)
        print("bot3 skaitļi:", bottom3)
        print("Vidējā vērtība:", videja_vertiba)
    except ValueError:
        print("Ievadiet derīgu skaitli!")