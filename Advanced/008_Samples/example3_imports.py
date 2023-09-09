# from mypackage.utils.long_names.physics.utils import too_long_foo_function, too_long_bar_function

# This is better
"""
from mypackage.utils.long_names.physics.utils import too_long_foo_function,\
    too_long_bar_function
"""

# This is the best
from mypackage.utils.long_names.physics.utils import (
    too_long_foo_function,
    too_long_bar_function
)


print(too_long_foo_function(1))
print(too_long_bar_function(2))
