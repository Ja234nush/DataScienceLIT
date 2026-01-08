
pesele=["92041812345", "85010154321", "78121698765"]
for i in pesele:
    poprawny_pesel = True
    if len(i) != 11: poprawny_pesel = False
    for j in i:
        if i.isdigit()==False:
            poprawny_pesel = False

    if poprawny_pesel: print(f"{i}:poprawny_pesel")
    else: print(f"{i}: niepoprawny pesel")