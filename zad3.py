lista=['python', 'java', 'python', 'javascript', 'python', 'java',
'c++', 'python']

czestosc={}
for slowo in lista:
    czestosc[slowo]=czestosc.get(slowo,0)+1
print(czestosc)