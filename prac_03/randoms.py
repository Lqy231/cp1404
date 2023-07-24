# help(random.randint)
# Help on method randint in module random:
# randint(a, b) method of random.Random instance
#     Return random integer in range [a, b], including both end points.

#
# help(random.randrange)
# Help on method randrange in module random:
# randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
#     Choose a random item from range(start, stop[, step]).
#
#     This fixes the problem with randint() which includes the
#     endpoint; in Python this is usually not what you want.


# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# all are integer. 5 is the smallest, 20 is the largest


# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# only 3, 5, 7, 9 are possible. 3 is the smallest, 9 is the largest. 4 is not possible


# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?

# float number. 2.5 is the smallest, 5.5 is the largest

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random     
print(random.randint(1, 100))
