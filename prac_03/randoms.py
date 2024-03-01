# 1
# This line produces a random integer between 5 and 20, inclusive of both endpoints.
#  The smallest number is 5, and the largest is 20.

# 2
# This line produces a random integer from the range 3 to 10, exclusive of 10, with a step of 2. This means it can produce numbers like 3, 5, 7, 9..
# The smallest number is 3, and the largest is 9.
# No, because the step is 2 starting from 3, so it skips over 4.

# 3
# This line produces a random floating-point number between 2.5 and 5.5, including both 2.5 and 5.5.
# The smallest number is 2.5, and the largest is 5.5.

import random
print(random.randint(1, 100))
