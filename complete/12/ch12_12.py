# queue
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.apppend(3)
print(q)
print(q.popleft())
print(q)

print('------------')
# defaultdict
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
d['b'] += 1
print(d['a'], d['b'], d['c'])

print('------------')
# ordereddict
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

print('------------')
# counter
from collections import Counter
fruits = ['apple', 'banana', 'apple','orange','banana', 'apple']
cnt = Counter(fruits)
print(cnt)
