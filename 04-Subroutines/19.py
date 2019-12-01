def suma(N):
    if N < 1:
        return 'Błędny argument'
    elif N == 1:
        return 1
    else:
        return N + suma(N-1)
    
print(suma(500))