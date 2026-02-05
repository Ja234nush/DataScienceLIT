import numpy as np
import matplotlib.pyplot as plt
import scipy as stats

n=1000
mi=50
sq=10
np.random.seed(42)
samples= np.random.normal(mi,sq,n)
suma=sum((samples<60) & (samples>40))
print(suma*100/n)

plt.hist(suma)
plt.show()