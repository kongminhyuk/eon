import numpy as np
# import random
import matplotlib.pyplot as plt

#class kongminhyuk:
#def init(self):
#self.num = int(input("N에 따라 달라지는 그래프, N을 입력해주세요"))

n=int(input("N값을 입력하시오:"))

np.random.seed(333)
a =np.random.randn(n)

mu1, sigma1 = np.mean(a) , np.std(a)
#def getGauss() :
    #데이터 얻기
print('평균:', np.mean(a))
print('표준편차:', np.std(a))
print('분산:', np.var(a))

plt.style.use('default')
plt.rcParams['figure.figsize'] = (6, 3)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 5

mu = 0.0
sigma = 1.0

x = np.linspace(-8, 8, n)
y = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-(x-mu)**2 / (2 * sigma**2))

Y2 = (np.random.normal(mu1, sigma1, n))

plt.plot(x, y, alpha=0.7, label='PDF of N(0, $1^2$)')
plt.hist(Y2, bins=1000, density=True, histtype='stepfilled', label=r'Follwing of N', color='C2')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-4.0, 4.0)
plt.legend(loc='upper left')
plt.show()

        #데이터 평균값, 분산값, print
        # random.gauss()
        
        #히스토그램 그래프 그리기