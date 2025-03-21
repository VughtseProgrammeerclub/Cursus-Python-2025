lengte = float(input("Geef je lengte op in meter, bijvoorbeeld 1.73: "))
gewicht = float(input("Geef je gewicht op in kilo, bijvoorbeeld 66.8: "))

bmi = gewicht / (lengte * lengte)
print(f"Je BMI is: {bmi:.2f}")
