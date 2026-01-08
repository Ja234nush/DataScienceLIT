kwoty=[1200, 1350, 1290, 1480, 1520, 1510, 1680,1720, 1700, 1890, 1950, 2100]
for i in range (1,len(kwoty)):
    if kwoty[i] > kwoty[i-1]:
        procent=(kwoty[i]-kwoty[i-1])/(kwoty[i])*100
        print(f"{i} {kwoty[i]:.2f} {procent:.2f}%")