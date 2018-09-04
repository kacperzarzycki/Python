numbers = [1, 2, 3, 4, 5, 6]
condition = lambda a: a+a==4 or a+a==6
answer = list(filter(condition, numbers))
print(answer)
