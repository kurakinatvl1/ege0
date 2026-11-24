from itertools import *
for val in product ('фокус',repeat = 5):
    val = ''.join(val)

for pos,val in enumerate(product('фокус',repeat = 5)):
     val = ''.join(val)
    # product щрмирует все возможные комбинации с повторениями