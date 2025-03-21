import math

invoer = input("Geef een getal op: ")
try:
    invoer_getal = int(invoer)
except:
    print("Invoer is geen nummer")
    exit()
    
if invoer_getal <= 1:
    print("Geen priem")
    exit();
    
for deler in range(2, math.ceil(math.sqrt(invoer_getal))):
    if invoer_getal % deler == 0:
        print("Geen priem")
        exit()

print("Priem")