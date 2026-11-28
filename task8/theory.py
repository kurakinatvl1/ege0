from itertools import *

alph = sorted('abc')

alph = sorted('abs',reverse=True)
alph = sorted(alph)[::-1]

for val in product ('фокус',repeat = 5):
    val = ''.join(val)

for pos,val in enumerate(product('фокус',repeat = 5)):
     val = ''.join(val)
    # product щрмирует все возможные комбинации с повторениями