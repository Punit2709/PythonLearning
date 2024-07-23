
f= open('Harry/sample.txt' ,'r+')
# data = f.read()
# print(data)

# f.write(" Aur Padhai Kesi Chal Rahi Hai")
# print(f.read())
# you can only read once  but write can be multiple times
print(f.readline())
print(f.readline())
print(f.readline())
# print(f.read(10))  #print First Five Char
f.close()


# modes of opening a file
# r - read mode    (can only read)
# a - append Mode (add content at the end of file)
# w - write mode   (clear previous content and Add new)
# + can be use (r + w)

# 'rb'  read binary
# 'rt'  read text file and default 