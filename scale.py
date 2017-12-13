import assets
from fingering import fingers
import convert
class scale:

    def __init__(self,*notes):
        self.notes = scale.__number__(notes)
        self.raw_intv = self.ri()
        self.root = self.notes[0]

    #takes notes from notes to numbers
    def __number__(notes):
        try:
            return list(map(int,notes))
        except ValueError:
            notes = list(map(convert.num_note,notes))
            for i in range(len(notes)-1):
                if notes[i] > notes[i+1]:
                    notes[i+1] += 12
            return notes

    #finds raw intervals
    def ri(self):
        notes = self.notes
        try:
            return self.raw_intv
        except AttributeError:
            root = self.notes[0]
            return list(map(lambda x: x-root,self.notes))

    #returns new scale with given root
    def transpose(self,n):
        if type(n) != int:
            n = convert.num_note(n)
        return scale(*list(map(lambda x: x+n,self.raw_intv)))

    #prints scale in proper way
    def output(self,flag = 'use_simple',notation = 'flats'):
        """Flags are:
            'use_simple'
            'use_proper'"""
        out = []
        note_nums = tuple(assets.inotes.values())

        if flag == 'use_simple':
            return list(map(lambda x: convert.simple_note_name(x,notation = notation),self.notes))

        elif flag == 'use_proper':
            
            if self.notes[0]%12 in assets.notes.keys():
                d_n = self.notes[0]%12
            elif notation == 'flats':
                d_n = (self.notes[0]+1)%12
            elif notation == 'sharps':
                d_n = (self.notes[0]-1)%12

            offset = note_nums.index(d_n)

            for index in range(len(self.notes)):
                count = (offset + index)%len(note_nums)
                d_l = note_nums[count]
                current_note = self.notes[index]
                out.append(convert.complex_note_name(current_note,d_l,notation = 'auto'))

            return out

    def fingers(self,fund):
        return list(map(lambda x: fingers(x,fund),self.notes))
