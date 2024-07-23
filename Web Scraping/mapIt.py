import webbrowser,sys,pyperclip

# we are gointg to street in Map by Giving Street Add in command line
# 'https://www.google.com/maps/place/your_address_string'
# if command line not having Address it will copy from ClipBoard

if len(sys.argv) > 1 :
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

print(sys.argv)
webbrowser.open('https://www.google.com/maps/place/'+ address)