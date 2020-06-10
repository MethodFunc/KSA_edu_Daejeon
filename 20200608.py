def factorio(n):
    if n==1 :
        return n
    else:
        res = n
        for i in range(n-1, 1, -1):
            res *= i

        return res

def prime_chk(n):
    i = 2

    while i <= 2:
        if n % i == 0:
            chk = False
            break
        else:
            i += 1

    if(n == i):
        chk = True

    return chk

print(factorio(4))

print(prime_chk(4))