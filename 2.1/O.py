N = int(input())
M = int(input())
T = int(input())

time = N * 60 + M + T
h = (time // 60) % 24
m = time - (time // 60) * 60

print(f"{h:0>2}:{m:0>2}")
