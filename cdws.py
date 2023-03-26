# def create_phone_number(n):
#     a = ""
#     a = a + "(" + str(n[0]) + str(n[1])+ str(n[2])+ ") "+ str(n[3])+  str(n[4])+ str(n[5]) + "-" + str(n[6])+ str(n[7])+ str(n[8])+ str(n[9])
#     return a
# value = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
# a = create_phone_number(value)
# print(a)


def square_digits(num):
    num1 = str(num)
    result = ""
    for item in num1:
        a = int(item)^2
        result = result + str(a)
    return result
nm = 4
a = square_digits(nm)
print(a)

# d = 123
# d1 = str(d)
# print(d1, type(d1))