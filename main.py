a = [1,2.3]
b = [10,20,30]

v = {a[key]: b[key] for key in range(len(a))}
print(v)