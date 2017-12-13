from fingering import fingers
from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))
##for i in range(200):
##    print(fingers(i,22)+1)
valves = [2,1,3,5]
dic = {}
altdic = {}
for comb in powerset(valves):
    hs = sum(comb)
    comb = tuple(map(lambda x: valves.index(x)+1,comb))
    try:
        dic[hs] += [comb]
    except KeyError:
        dic[hs] = [comb]
    try:
        if len(altdic[hs]) > len(comb):
            altdic[hs] = comb
    except KeyError:
        altdic[hs] = comb
