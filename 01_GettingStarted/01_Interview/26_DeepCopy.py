# Refer: https://hi-techjob.com/cms/page/50-cau-hoi-python/

import copy

# Using '=' operator
x = [1, 2, 3]
y = x
x[0] = 5    # value of 'y' also changes as it is the SAME object
x[1] = 15
print "Shallow copy: ", y

# Using copy.deepcopy()
a = [10, 20, 30]
b = copy.deepcopy(a)
a[1] = 70   # value of 'b' does NOT change because it is ANOTHER object
print "Deep copy: ", b
