import re
from assets import notes,inotes,sign
from math import log
pat = r'(?P<note>[a-gA-G]{1})(?P<mod>[♭#]*)(?P<octave>\d*)'
pat = re.compile(pat)
tuning_a = 440

def num_note(n):
    rpat = r'[^A-Ga-g#♭\d]'
    n = re.sub(rpat,'',n).upper()
    n = pat.match(n).groupdict()
    note = inotes[n['note']]
    mod = n['mod']
    octave = n['octave']
    if octave:
        octave = int(octave)
    else:
        octave = 0
    if mod:
        change = sign[mod[0]]*len(mod)
    else:
        change = 0
    return 12*octave+change+note

def simple_note_name(n,notation = 'flats'):
    if notation not in ('sharps','flats'):
        raise ValueError('Notation flag is either "sharps" or "flats."')

    octave = str(n//12)
    n %= 12

    if n in notes.keys():
        note = notes[n]
        mod = ''
    
    elif notation == 'flats':
        note = notes[(n+1)%12]
        mod = '♭'
    elif notation == 'sharps':
        note = notes[(n-1)%12]
        mod = '#'
    return note+mod+octave

def complex_note_name(n,note,notation='auto',overkill= False):
    if notation not in ('sharps','flats','auto'):
        raise ValueError('Notation flag is either "sharps","auto" or "flats."')
    if type(note) == str:
        note = note.upper()
        d_n = inotes[note]
    else:
        d_n = note
        note = notes[note]
        
    octave = n//12
    modify_n = (n-d_n)%12

    #complex bit
    if notation == 'flats':
        modify_n_new = modify_n%(-12)
        if modify_n != modify_n_new:
            octave += 1
        modify_n = modify_n_new
    elif notation == 'sharps':
        modify_n_new = modify_n%(12)
        if modify_n != modify_n_new:
            octave -= 1
        modify_n = modify_n_new
    else:
        if modify_n > 7:
            modify_n %= -12
    #just formating from here on out
    if modify_n < 0:
        mod = '♭'*abs(modify_n)
    elif modify_n > 0:
        mod = '#'*modify_n
    else:
        if overkill:
            mod = '♮'
        else:
            mod = ''
    octave = str(octave)
    return note+mod+octave
