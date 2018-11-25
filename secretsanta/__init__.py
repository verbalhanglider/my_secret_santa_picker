
from random import shuffle, choice

def assign(participants):
    """a method to take a list of participants and return gift giver and reciever

    :param participants: an iterable containing strings to match up
    :type participants: list
    :return: a set of key:value pairs representing a secret santa giver and 
     their gift gift reciever
    :rtype list
    """
    out = dict()
    shuffle(participants)
    givers = []
    receivers = []
    for i in range(len(participants) - 1):
        giver = participants[i]
        receiver = participants[i+1]
        out[giver] = receiver
        givers.append(giver)
        receivers.append(receiver)
    giver_not_getting_gift = set(givers).difference(set(receivers))
    receiver_not_giving = set(receivers).difference(set(givers))
    if len(giver_not_getting_gift) > 0 and len(receiver_not_giving) > 0:
        merged = zip(list(receiver_not_giving), list(giver_not_getting_gift))
        for giver, receiver in merged:
            out[giver] = receiver
    return out
