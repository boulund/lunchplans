# Lunchplans at MV
This program collects and presents a summary of today's lunch menus at
different lunch restaurants around Chalmers. 

Requires Python 2.7 with:

  * beautifulsoup4
  * requests

The program has no other dependencies and should be fairly straightforward
to get running after download. To download a clone of the bitbucket repository,
run `hg clone http://bitbucket.org/chalmersmathbioinformatics/lunchplans`. 


## What does it do?
The main goal was to produce a simple program that could generate a listing of
available lunch options for the day.

Currently it can:

  * collect lunch menus from websites and combines them into a single summary. 
  * send email(s) with the summary to one or more adresses.


## Authors
Fredrik Boulund
Tobias Abenius
Tobias Österlund
*<your name here>*


## Usage
To use the lunchbot, clone the repository into a folder of your choice, run
`lunchplans.py` from inside that folder. It will then print a summary of
today's lunch options to stdout. Use `-h` to see additional options.


### Automate it
You can setup a cronjob to run it at a suitable time every weekday, e.g. around
10.45. Run `crontab -e` to edit your cron table and add a line to make it run
every weekday. For example:

    45 10 * * mon,tue,wed,thu,fri /path/to/repository/lunchplans.py

## Contribute
Details for how to contribute to the project are located in CONTRIBUTING.md
