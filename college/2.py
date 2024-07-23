print('1. Celsius to Fahrenheit') 
print('2. Fahrenheit to Celsius')

ch = int(input('Enter your choice: ')) # F == 1.8 * c + 32
if ch==1:
    cel = float(input('Enter temprature in Celsius: ')) 
    fah = (1.8 * cel) + 32
    print('Temprature in Fahrenheit: ',fah) 
else:
    fah = float(input('Enter temprature in Fahrenheit: ')) 
    cel = (fah - 32) / 1.8
    print('Temprature in Celsius: ',cel)
