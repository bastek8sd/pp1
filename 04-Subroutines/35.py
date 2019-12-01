def sumaCyfr(val, prev=0):
    if val == 0:
        return 0
    suma = val % 10
    return suma + sumaCyfr(int(val/10), suma)

print(sumaCyfr(789))