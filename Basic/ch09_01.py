# in this file contains twinke twinkle poem so checking is twinkle in persent or not
 
f = open('Harry/poem.txt','r')
data = f.read()

if 'twinkle' in data :
    print('Present')
else :
    print('Absent')

f.close()  # always close the file 