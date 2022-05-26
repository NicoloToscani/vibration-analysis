t_first = int(input('t_first: '))
t_last = int(input('t_last: '))

x_first = float(input('x_first: '))
x_last = float(input('x_last: '))

t_missing = int(input('t_missing: '))

x_missing = x_last + ((x_last - x_first) / (t_last - t_first)) * (t_missing - t_last)

print("x_missing: " + str(x_missing))
