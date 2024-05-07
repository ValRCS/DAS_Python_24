tempC=float(input("Kāda ir temperatūra Celsija grādos? "))
tempF=32+tempC*(9/5)
tempF=round(tempF, 2) # of course 2 could be some VARIABLE like PRECISION
 
print(f"Celsija {tempC} C° pārrēķinot pēc Farenheita būs {tempF} F°")