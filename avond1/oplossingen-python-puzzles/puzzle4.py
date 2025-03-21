vorig_nummer = 0
nummer = 1
som = 1

print(f"0: {vorig_nummer}")
print(f"1: {nummer}")

for i in range(2, 20):
    volgend_nummer = vorig_nummer + nummer
    print(f"{i}: {volgend_nummer}")
    vorig_nummer = nummer
    nummer = volgend_nummer
    som = som + nummer

print(som)
