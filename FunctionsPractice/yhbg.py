def nthf(n):

    if n == 1 or n == 2:
        return 1
    else:
        return nthf(n-1) + nthf(n-2)

print(nthf(12))