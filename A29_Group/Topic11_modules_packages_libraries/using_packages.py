# packages are simply directories with optinal __init__.py file

# to use package we need to import it

import my_package.my_mod1

my_package.my_mod1.my_mod1_greet("Valdis")

# even better would be to import with alias
from my_package import my_mod2 as mm2
# now I can call it directly
mm2.my_mod2_greet("Valdis")

# i could even import specific functions/classes/constants from the module inside package
from my_package.my_mod2 import E
print(E)