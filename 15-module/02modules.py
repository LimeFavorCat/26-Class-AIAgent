# 1
import modules.my_module2
modules.my_module2.my_func()

# 2
import modules.my_module2 as m
m.my_func()

# 3 
from modules.my_module2 import my_func
my_func()

# 4
from modules.my_module2 import my_func as m
m()

