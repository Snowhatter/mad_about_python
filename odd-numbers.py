print('enter two numbers')

l = int(input().strip())
r = int(input().strip())


while l <= r:
    if l%2 != 0:
        print(l)
    l = l + 1