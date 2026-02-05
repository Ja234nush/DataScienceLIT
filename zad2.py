import numpy as np
import matplotlib.pyplot as plt
import scipy as stats

n=1000
mi=100
sq=15
np.random.seed(42)
samples= np.random.normal(mi,sq,n)

lessthan85=np.less(samples,85)
morethan120=np.greater(samples,120)
lessthan110morethan90=np.greater(np.less(samples,110),90)
print("lessthan85",sum(lessthan85)*100/n)
print("morethan120",sum(morethan120)*100/n)
print("lessmore",sum(lessthan110morethan90)*100/n)
