sq = list(map(lambda x:x ** 2, range(10)))
sq2 = [x **2 for x in range(10)]
sq3 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
sq4 = [(x,y)for x in[1,2,3] for y in[3,1,4]]
sq5 = {x:x**2 for x in (2,4,6)}
sq6 = dict([(1,2),(3,4),(5,6)])

print(sq)
print(sq2)
print(sq3)
print(sq4)
print(sq5)
print(sq6)