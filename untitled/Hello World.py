import numpy as np

import matplotlib as mlp

t = [5, 'string', 7.0]

q = np.array([5, 6, 7, 8])
g = np.matrix(q)

q = np.array([[1,1], [-1, 1]])
gq = np.matrix(q)
print(gq)
print(gq.I)

print(g)
#def pp(aaa):
#    print(aaa)
#    return;

#for a in range(1, 10):
#    print(a)
#    pp(a+1)

