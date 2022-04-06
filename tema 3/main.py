from my_package.my_module import *

def your_function(*args, **kwargs):
    sum = 0
    for arg in args:
        if (isinstance(arg, int) or isinstance(arg, float)):
            sum = sum + arg
    return sum

print(your_function(1, 5, -3, "abc", [12, 56, "cad"]))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))
# 1

def verif():
    nr = input("Introduceti un numar: ")
    try:
        isinstance(nr, int)
        print(nr)
    except:
        print(0)


verif()
# 2

print(sum(10))
print(sum_pare(10))
print(sum_impare(10))