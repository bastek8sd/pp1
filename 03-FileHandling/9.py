i = 1
with open('NoEducation.txt','r') as file:
    for line in file:
        print(f"{i} {line}", end='')
        i = i + 1