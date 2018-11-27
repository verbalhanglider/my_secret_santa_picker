# Secret Santa

A quick-n-dirty secret Santa assignment tool that is meant to be run on the 
command-line.

Prerequisite:

1. Login to your Goopgle Account and create an App-specific password for this application to use.
2. Be sure and save that password because you're going to need it later!

Then, do the following on the command-line:

```bash
$ mkdir ~/.local/share/SecretSanta
$ echo "[Configuration]" >> ~/.local/share/SecretSanta/config.ini
$ echo "email_sender_address=your_gmail_address" >> ~/.local/share/SecretSanta/config.ini
$ echo "email_sender_password=an_app_specific_password" >> ~/.local/share/SecretSanta/config.ini
$ git clone https://github.com/verbalhanglider/my_secret_santa_picker.git
$ cd my_secret_santa_picker
$ python3 -m venv venv
$ source venv/bin/activate
$ python setup.py install
$ python bin/run_assignments Janet:janet@doe.com,Bill:bill@example.com,Erica:erica@example.com
```

Jane, Bill and Erica will all receive email addresses informing them of who 
they are Secret Santa for.
