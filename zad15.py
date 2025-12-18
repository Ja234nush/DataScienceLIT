dzien1 = {'user001', 'user002', 'user003', 'user004', 'user005', 'user010'}
dzien2 = {'user002', 'user003', 'user006', 'user007', 'user008', 'user010'}
dzien3 = {'user003', 'user004', 'user009', 'user010', 'user011'}



wszystkie_dni = dzien1 & dzien2 & dzien3


tylko_d1 = dzien1 - (dzien2 | dzien3)
tylko_d2 = dzien2 - (dzien1 | dzien3)
tylko_d3 = dzien3 - (dzien1 | dzien2)


razem_tylko_jeden = tylko_d1 | tylko_d2 | tylko_d3


d1_d2 = (dzien1 & dzien2) - dzien3
d1_d3 = (dzien1 & dzien3) - dzien2
d2_d3 = (dzien2 & dzien3) - dzien1

dokladnie_dwa = d1_d2 | d1_d3 | d2_d3


print(f"\n1. Aktywni przez wszystkie 3 dni ({len(wszystkie_dni)}):")
print(f"   {sorted(list(wszystkie_dni))}")

print(f"\n2. Aktywni w dokładnie 2 dniach ({len(dokladnie_dwa)}):")
print(f"   {sorted(list(dokladnie_dwa))}")

print(f"\n3. Aktywni tylko w 1 dniu (szczegóły):")
print(f"   - Tylko Dzień 1: {sorted(list(tylko_d1))}")
print(f"   - Tylko Dzień 2: {sorted(list(tylko_d2))}")
print(f"   - Tylko Dzień 3: {sorted(list(tylko_d3))}")