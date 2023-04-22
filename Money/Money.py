#4 5 5 5
#0
#4 6 6 6
#50 1 8 5 50 15 23 7 49 44 10 20 25 13 14 4 22 17 3 29 11 24 27 45 28 46 9 30 48 35 42 31 21 33 32 40 38 26 12 36 16 6 39 43 19 37 2 47 41 34 18
#3 2 1 2
n1, *c = map(int, input().split()) 
k1, *a = map(int, input().split()) 
n2, *d = map(int, input().split()) 
k2, *b = map(int, input().split()) 
e = list(map(int, input().split())) 


def is_unlucky(number, unlucky_numbers):
    return number in unlucky_numbers

k = len(c) 
x = e[0] 
for i in range(1, k):
    if not is_unlucky(i, a): 
        x += e[i] * c[i-1]
k = len(d) 
s = [0] * k 
for i in range(k-1, 0, -1):
    if not is_unlucky(i, b): 
        s[i] = x % d[i-1]
        x //= d[i-1]
s[0] = x 
print (s) #52 0 0 0