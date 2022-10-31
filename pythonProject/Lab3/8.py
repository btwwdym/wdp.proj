l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]
l3 = []
for i in l1:
    l3.append(i) if i % 2 != 0 else l3
for i in l2:
    l3.append(i) if i % 2 == 0 else l3
print(l3)
