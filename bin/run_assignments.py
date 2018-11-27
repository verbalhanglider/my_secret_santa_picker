"""a CLI for Secret Santa assignments
"""

from appdirs import user_data_dir
from argparse import ArgumentParser
from datetime import datetime
from configparser import ConfigParser
from os import _exit
from os.path import exists, join
import smtplib
from sys import argv, stdout

import secretsanta

__AUTHOR__ = "Tyler Danstrom"
__APP__ = "SecretSanta"


def get_configuration():
    """get configuration info for how to send the email 

    Config directory is .local/share/SecretSanta
    """
    config_dir = user_data_dir(__APP__, __AUTHOR__)
    config_file = join(config_dir, 'config.ini')
    if exists(config_file):
        config = ConfigParser()
        config.read(config_file)
        sender_email = config.get('Configuration', 
                'email_sender_address')
        sender_password = config.get('Configuration', 
                'email_sender_password')
        return sender_email, sender_password

def sendmail(message, email_address, sender, password):
    """quick hack to send email using Google's SMTP server and sender's account

    To use this sender must have a App specific password defined and entered 
    in the config.ini file in the app's data directory
    """
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)
    message = message
    s.sendmail("sender_email_id", email_address, message)
    s.quit

def main():
    arguments = ArgumentParser(\
            description="A tool to draw Secret Santa assignments", 
            epilog="Written by {}".format(__AUTHOR__))
    arguments.add_argument("participants", 
            help="Enter a list of the participants with each participant " +\
                 " like so: Name:email. Ex: tyler:tyler@danstrom.com",
            default=[],
            type=str,
            nargs="+")
    parsed_args = arguments.parse_args()
    try:
        sender, password = get_configuration()
        participants = dict([tuple(x.split(':')) for x in parsed_args.participants])
        assignments = secretsanta.assign([k for k in participants])

        for giver,receiver in assignments.items():
            message_body = "Dear {},\n\nYou are Secret Santa for {}.\n\nThat meanst that you should send a present for that person to open on Christmas Day.\n\nRules for Secret Santa are:\n\n1. Price limit of $80.\n2. Don't tell anyone who you are Secret Santa for.\n\nMerry Christmas!\nSecret Santa Assignment".format(giver[0].upper()+giver[1:], receiver[0].upper()+receiver[1:])
            address = participants.get(receiver)
            message = "From: " + sender + "\nTo: " + address + "\nSubject: Danstrom sibling gift exchange\nDate: " + datetime.now().isoformat() + "\n\n" + message_body

            sendmail(message, address, sender, password)
        stdout.write("INFO -- sent assignments to %s" % ', '.join(participants))
        return 0
    except KeyboardInterrupt:
        return 131

if __name__ == "__main__":
    _exit(main())
