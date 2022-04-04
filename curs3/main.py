from my_package.my_module import my_var as module_var, my_func as my_module_func
from my_package.my_second_module import *

if __name__ == '__main__':
    print('Ok')
    print(module_var)
    print(my_module_func())