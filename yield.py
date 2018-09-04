def my_range(x):
    a = 1
    while a!=x:
        yield a
        a+=1

x = int(input('Give me a range: '))
for number in my_range(x):
    print(number)
input()
