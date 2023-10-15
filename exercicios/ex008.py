def metros(x):
    print(x)


mm = int(input("Uma distancia em metros: "))
print(f"A media de {mm}m corresponde a")
metros(f"{mm / 1000}km")
metros(f"{mm / 100}hm")
metros(f"{mm / 10}dam")
metros(f"{mm * 10}dm")
metros(f"{mm * 100}cm")
metros(f"{mm * 1000}mm")