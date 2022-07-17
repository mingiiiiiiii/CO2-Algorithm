import sys
n, m = map(int, sys.stdin.readline().split())
dict1 = dict()
for i in range(n):
    dict1[sys.stdin.readline().rstrip()] = i
db = []
for i in range(m):
    try:
        temp = sys.stdin.readline().rstrip()
        dict1[temp]
    except:
        pass
    else:
        db.append(temp)
db.sort()
print(len(db))
for dbs in db:
    print(dbs)
