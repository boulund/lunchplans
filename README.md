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
*<your name here>*

## Contributors
Tobias Österlund
*<your name here>*


## Usage
To use the lunchbot, clone the repository into a folder of your choice, run
`lunchplans.py` from inside that folder. It will then print a summary of
today's lunch options to stdout.

### Automate it
You can setup a cronjob to run it at a suitable time every weekday, e.g. around
10.45. Run `crontab -e` to edit your cron table and add a line to make it run
every weekday. For example:

    45 10 * * mon,tue,wed,thu,fri /path/to/repository/lunchplans.py


## Contribute
You can contribue by writing a lunch restaurant module if you feel there is one
missing.

### TODO
Several things can be contributed by you:

  * Add more restaurant modules (lunch menu parsers/scrapers)
  * "Lunchbot"-code that suggests a lunchplace each day.
	 Can be expanded with lots of ideas; Markov chain-based etc.


## What can I do?
The following sections highlight some suggestions for areas that can be improved.

We store all notable modifications to the project in `CHANGELOG.md`, so make
sure to update it if you modify anything. There are some brief instructions in the
changelog file.


### Restaurant module
To create a restaurant module, copy one of the previous modules in
`restaurants` and modify it so it acts like the other restaurant modules.  When
you are done, add it to the import list in `restaurants/__init__.py`.  The
module will then be imported automatically in the main `lunchplans.py` program.


#### Restaurant API
All restaurant modules must conform to the same API.  Each restaruant is
defined in a separate file in the `restaurants` module.  They must provide
two things:

  * A function called `todays_lunch`
  * An attribute called `name`

The `todays_lunch` function takes no required arguments and returns a single
string, possibly with linebreaks to separate different menu options.
The name attribute is defined at the top level of the file and is just a 
string containing the restaurants name, keep it reasonably short.


### Markov chain-based recommendation lunchbot engine
There's been some talk about implementing a Markov chain-based "lunchbot" to
create a suitable lunch recommendation each day, removing the need for lengthy
discussions on Skype (potentially improving workplace productivity ;)).

### Doodle API
It would be cool to implement automatic Doodle poll generation.
Doodle has a Poll Wizard API that might be used to generate polls:

http://doodle.com/wizard/DoodleWizard.pdf

