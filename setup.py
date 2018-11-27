from setuptools import setup

setup(name="Secret Santa Generator",
      author="Tyler Danstrom",
      author_email="tyler@danstrom.com",
      version="1.1.0",
      description="A simple utility to take a list of participants and " +
                  "assign a Secret Santa  to each participant",
      packages=['secretsanta'],
      install_requires=['appdirs']
)
