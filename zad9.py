# %%

import numpy as np

slownik = {}

data = list(np.random.randint(1, 100, 10))
slownik["data"] = []
import numpy as np

data = list(np.random.randint(1, 100, 10))
slownik = {}

for x in data:
    slownik['data'] = slownik.get('data', []) + [x]

print(slownik)