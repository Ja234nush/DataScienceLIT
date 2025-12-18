slownik= {i: i*i for i in range(1,21)  }

print(slownik)

slownik_parzyste = {k: v for k, v in slownik.items() if k % 2 == 0}
print(slownik_parzyste)