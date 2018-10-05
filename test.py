# sl = [['zohamed', 37.21], ['reda', 37.21]]

# sl.sort()

# print(sl)


# from decimal import Decimal, ROUND_HALF_UP

# val = Decimal('1.45')

# Decimal(val.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

# val.quantize()
# Decimal('1.5')
from decimal import Context, Decimal, getcontext


val = 22.242 
val.quantize(Decimal('1.000'))

print(val)