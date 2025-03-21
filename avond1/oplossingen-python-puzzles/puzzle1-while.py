geheim_woord = "Frikandel"
invoer = input("Geef het geheime woord op: ")
aantal_pogingen = 1

while invoer != geheim_woord and aantal_pogingen < 3:
    invoer = input("Fout! Geef het geheime woord op: ")
    aantal_pogingen += 1
    
if aantal_pogingen == 3:
    print("Niet geraden")
else:
    print ("Goed zo!")
    