mas = input().split()
numbers = [int(x) for x in mas]
if numbers[0] % 2 == 0 and numbers[1] % 2 == 0:
    print(1)
elif numbers[0] % 2 != 0 and numbers[1] % 2 != 0:
    print(1)
else:
    print(0)
