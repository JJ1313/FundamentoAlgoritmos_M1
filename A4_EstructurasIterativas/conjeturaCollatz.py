n = int(input())

while True:
    print(int(n), end=' , ')
    # Calculo nuevo numero 
    if n%2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
    # Condicion de termino
    if n == 1:
        print(1, end='.')
        break