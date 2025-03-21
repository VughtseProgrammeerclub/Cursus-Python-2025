geheim_woord = "geheim"
for i in range(0,3):
    invoer = input("Geef het geheime woord op: ")
    if invoer == geheim_woord:
        print("Geraden!")
        exit()
    else:
        print("Fout!")
