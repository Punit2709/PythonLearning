


# great Problem 🔥🔥
# Statement :- Write a program to Write a table from 2 to 20 in different file and store in Folder

for i in range(11,41):
    with open(f'Basic/Tables/Table_of_{i}.txt' , 'w') as f:
        for j in range(1,11):
            f.write(f'{i}*{j} = {i*j}\n') 