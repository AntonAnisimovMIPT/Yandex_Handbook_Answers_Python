n = int(input())
m = int(input())
a = n % 10
b = m % 10
c = n // 10 % 10
d = m // 10 % 10
e = n // 100 % 10
f = m // 100 % 10
g = (a + b) % 10
h = (c + d) % 10
i = (e + f) % 10
print(f'{i}{h}{g}')
