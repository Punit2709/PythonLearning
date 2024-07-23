
with open('Harry/donkey.txt','r+') as f:
    content = f.read()

if ('Donkey' in content) :
        print('Yesss Present')
        content = content.replace('Donkey', 'Munna')
        with open('Harry/donkey.txt','w') as f:
            f.write(content)
        print('Kaam Ho gaya')
else:
    print('Not Present')
