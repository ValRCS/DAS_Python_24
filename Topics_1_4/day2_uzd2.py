
PRECISION = 2
# so we can convert in the same row that we get input
height=float(input("What is the height (in meters)?"))
width=float(input("What is the width?"))
lenght=float(input("What is the lenght?"))
volume=round(height*width*lenght, PRECISION)
print(f"Volume of the space is {volume} m³")