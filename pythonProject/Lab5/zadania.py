'''                                                        zad1'''
# l1 = [10, 20, 30]
# l2 = ['ten', 'twenty', 'thirty']
# a = dict(zip(l2, l1))
# print(a)
# b = dict(thirty=30, forty=40, fifty=50)
# print(b)
# for i, v in b.items():
#     print(i, v)
# a.update(b)
# print(a)
'''                                                        zad2'''
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
samd = ["name", "age"]
sd = {}
for f in samd:
    if f in sample_dict:
      sd.update(f)

print(sd)
