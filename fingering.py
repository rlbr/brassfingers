import convert

from math import log
def tune_harm(a_c,n):
    '''Function that gives the tuning of a harmonic in relation to it's
nearest equal temperment note.'''
    log_harm = a_c+12*log(n,2)
    equal_temp = round(log_harm)
    return (equal_temp,round(100*(log_harm-equal_temp)))

def fingers(n,ff):
    c = int(2**((n-ff)/12))
    if c <= 0:
        c = 1
    while True:
        current = tune_harm(ff,c)
        if current[0] >= n and abs(current[1]) <= 14:
            return current[0]-n
        c += 1
