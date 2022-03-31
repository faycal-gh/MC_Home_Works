def u(x):
  if x >= 0:
    if x == 0:
      return 0
    elif x == 1:
      return 1
    elif x == 2:
      return 2
    else:
      return 2*u(x-1) + 3*u(x-3)
x = 5
print(u(x))
