inotes = {"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
notes= {v: k for k, v in inotes.items()}
sign = {'#':1,'♭':-1}
minimal = {1: (2,),
 2: (1,),
 3: (3,),
 4: (2, 3),
 5: (4,),
 6: (2, 4),
 7: (1, 4),
 8: (3, 4),
 9: (2, 3, 4),
 10: (1, 3, 4),
 11: (1, 2, 3, 4)}

everything = {1: [(2,)],
 2: [(1,)],
 3: [(3,), (1, 2)],
 4: [(2, 3)],
 5: [(4,), (1, 3)],
 6: [(2, 4), (1, 2, 3)],
 7: [(1, 4)],
 8: [(3, 4), (1, 2, 4)],
 9: [(2, 3, 4)],
 10: [(1, 3, 4)],
 11: [(1, 2, 3, 4)]}
