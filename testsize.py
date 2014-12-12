import sys
from random import randint

N = 1

for n in range(N):
    n = 10 * (n+1)
    al = []
    am = {}

    for i in range(n):
        row = [randint(0,1) for x in range(n)]
        al.append(row)
        am[i] = dict([(k, v) for k,v in enumerate(row) if v is 1])

        sys.stdout.write("[%d]%s (%d)\n\n" % (i, al[i], len(al[i])))
        print am


    sys.stdout.write("%d\tal: %d\tam: %d\n" % (n, sys.getsizeof(al), sys.getsizeof(am)))
