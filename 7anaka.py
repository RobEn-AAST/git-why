def powerOptimised(a, n):
    ans = 1
    while (n > 0):
        last_bit = (n & 1)
        if (last_bit):
            ans = ans * a
        a = a * a
        n = n >> 1
    return ans

x = powerOptimised(3, 2)
print(x)
