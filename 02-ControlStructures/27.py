for x in range(1,10):
    if x in [int(a) for a in range(1,6)]:
        for y in range(0,x):
            print('*', end=' ')
    else:
        for y in range(x,10):
            print('*', end=' ')
    print()