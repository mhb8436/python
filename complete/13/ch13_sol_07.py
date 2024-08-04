try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

try:
    elist = [1.2]
    print(elist[5])
except IndexError as e:
    print(e)

try:
    edict = {'a':1}
    print(edict['b'])
except Exception as e:
    print(e)

try:
    print("hello" + 1)
except:
    print('error')

try:
    import math
    print(math.sqrt(-10))
except ValueError as e:
    print('error', e)
else:
    print('success')





