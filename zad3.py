import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

np.random.seed(9)
n = 500
cena = np.random.uniform(50, 200, n)
reklama = np.random.uniform(100, 5000, n)
sezon = np.random.randint(1, 5, n)
szum = np.random.normal(0, 50, n)
sprzedaz = -2*cena + 0.5*reklama + 100*sezon + 5000 + szum
X=pd.DataFrame({'cena':cena,'reklama':reklama,'sezon':sezon})
model=LinearRegression().fit(X,sprzedaz)
coeffs = dict(zip(X.columns, model.coef_))
print(f"Interpretacja współczynników:")
print(f"- Cena ({coeffs['cena']:.2f})")
print(f"- Reklama ({coeffs['reklama']:.2f})")
print(f"- Sezon ({coeffs['sezon']:.2f})")

# 3. Odpowiedź na pytanie biznesowe
wzrost_reklamy = 1000
przewidywany_wzrost = wzrost_reklamy * coeffs['reklama']
print(f"\nOdp: Jeśli zwiększymy budżet reklamowy o 1000, sprzedaż wzrośnie o {przewidywany_wzrost:.0f} jednostek.")