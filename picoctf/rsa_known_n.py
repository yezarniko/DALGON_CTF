import math
import gmpy2

c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
N = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923

# common
e = 65537

# calculate p and q from http://factordb.com/
p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033

pi = (p-1)*(q-1)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def calculate_d(p, q, e):
    phi = (p - 1) * (q - 1)
    _, d, _ = extended_gcd(e, phi)
    return d % phi

d = calculate_d(p, q, e)
print("The value of d is:", d)


m = pow(c, d, N)
decrypted_text = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode("utf-8")


print("m = ", m)
print("decrypted_text = ", decrypted_text)
