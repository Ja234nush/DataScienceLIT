import time

list=list(range(1,11))
tuple=tuple(list)
sett=set(list)
print(list)
print(tuple)
print(sett)

start=time.time()
5 in list
end=time.time()
czas_lista=end-start


start=time.time()
5 in tuple
end=time.time()
czas_tuple=end-start

start=time.time()
5 in sett
time.sleep(1)
end=time.time()
czas_set=end-start
print(f"Czas dla listy:   {czas_lista:.20f} s")
print(f"Czas dla krotki:  {czas_tuple:.20f} s")
print(f"Czas dla zbioru:  {czas_set:.20f} s")