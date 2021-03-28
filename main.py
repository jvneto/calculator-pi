from decimal import Decimal, getcontext
import time

init_time = int(round(time.time()))

getcontext().prec = 1000
pi = (sum(1/Decimal(16)**k *
          (Decimal(4)/(8*k+1) -
           Decimal(2)/(8*k+4) -
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(1000)))

open('pi.txt', 'w').write(str(pi))

print(f'tempo: {int(round(time.time())) - init_time} segundos para calcular que pi = {round(pi)}')
