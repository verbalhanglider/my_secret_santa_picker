
import secretsanta
from sys import argv, stdout

if __name__ == "__main__":
    participants = argv[1]
    participants = participants.split(',')
    assignments = secretsanta.assign(participants)
    for k,v in assignments.items():
        stdout.write("{} buys for {}.\n".format(k,v))
