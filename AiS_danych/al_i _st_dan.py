# if __name__== "__main__":
#     x = 3
#     print(x)
#     print(type(x), "\n")
#     x = 3.4
#     print(x)
#     print(type(x), "\n")
#     x = [1,2,3]
#     print(x)
#     print(type(x), "\n")
#     x = (1,2,3)
#     print(x)
#     print(type(x), "\n")
#     x = {1,2,3}
#     print(x)
#     print(type(x))


# if __name__ == "__main__":
#  collection = (1,2,3)
#  a = collection[0]
#  b = collection[1]
#  c = collection[2]
#  x, y, z = collection
#  print(f"a = {a}, b = {b}, c = {c}")
#  print("x =", x, ",y =", y, ",z =",z) 


from time import sleep
from datetime import datetime
if __name__ == "__main__":
 while True:
    print(datetime.now().strftime("%H:%M:%S"))
    sleep(1) 

