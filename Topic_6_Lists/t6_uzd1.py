skaitli = []
 
while True:
    ievade = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if ievade.lower() == 'q':
        break
    try:
        skaitls = float(ievade)
        skaitli.append(skaitls)
        videja_vertiba = sum(skaitli) / len(skaitli)
        print("Visi skaitļi:", skaitli)
        print("Vidējā vērtība:", videja_vertiba)
    except ValueError:
        print("Ievadiet derīgu skaitli!")