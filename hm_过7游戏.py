i = 1
while i <= 99:
    if i % 7 == 0 or str(i).find('7') != -1:
        print('过')
    else:
        print(i)
    i += 1
