def gcd(n, m):
    c, d = min(n, m), max(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return c

def solution(w,h):
    return w * h - (w + h - gcd(w,h))