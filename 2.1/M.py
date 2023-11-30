children = int(input())
candies = int(input())

per_child = candies // children
remainder = candies - per_child * children
print(per_child)
print((remainder))
