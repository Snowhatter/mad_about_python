num = '9,223,ad 2345:040 9456, 8887; 908'
sep = ''
for n in num:
    if not n.isnumeric():
        sep = sep + n

print(sep)

values = "".join('seeta','geeta')

print(values )