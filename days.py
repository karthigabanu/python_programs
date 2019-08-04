#calculate number of days between two dates.
from datetime import date
f_date=date(2000,5,28)
l_date=date(2019,8,3)
a=l_date - f_date
print(a.days)
