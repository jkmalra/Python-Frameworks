import math

n = 15

if (n % 2) == 0:
    print("weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("no weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("weird")
elif n % 2 == 0 and n > 20:
    print("not weird")