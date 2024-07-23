import time 
import calendar

gf_bd = '18 December, 1950'
gf_bd_yr = time.strptime(gf_bd,'%d %B, %Y') 
cyr = time.localtime()


print('Grandfather age is: ',(cyr.tm_year - gf_bd_yr.tm_year)) 
print(f'\n',calendar.month(1950,12))
