import numpy as np

TRIES = 100000000
PROB = 1. / 3

a = np.random.binomial(1, PROB, TRIES)
b = np.random.binomial(1, PROB, TRIES)
c = np.random.binomial(1, PROB, TRIES)
d = np.random.binomial(1, PROB, TRIES)

success = 0
for i in range(TRIES):
    if a[i] == 0 and b[i] == 1 and c[i] == 1 and d[i] == 1:
        success += 1

print "%d / %d" % (success, TRIES)
print (0. + success) / TRIES
