def fibR(n, prev=[0, 1]):
    if n == 1:
        return prev[0]
    else:
        a = prev[1]
        b = prev[0]+prev[1]
        return fibR(n-1, [a, b])
    
for n in range(1, 21):
    print(fibR(n), end=' ')