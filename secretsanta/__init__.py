
from random import shuffle 

def assign(participants):
    participants = list(set(participants))
    out = dict()
    for i in range(len(participants) -1):
        giver = participants[i ]
        receiver = participants[i+1]
        out[giver] = receiver
    return out
