# Lunchplans at MV
Presents a Doodle poll everyday with today's lunch options
presented in a nice way. 

Requires Python 2.7 with:

  * beautifulsoup4
  * requests


## What does it do?
Generate a listing of available lunch options inside a Doodle poll
with Yes, No, Maybe options for participants to make it quick and easy
to decide on a lunch restaurant.

## Authors
Fredrik Boulund  
<your name here>

## Usage
To use the lunchbot, clone the repository into a folder of your choice, then
setup a cronjob to run it at a suitable time every weekday, e.g. around 10.45.
Like so:

    45 10 * * mon,tue,wed,thu,fri /path/to/repository/lunchplans.py

It expects two files in the base directory: `other.txt` and `mailinglist.txt`.
The file `other.txt` contains one restaurant name per line, for restaurants that
do not have an online menu or haven't yet been given their own restaurant module.
The file `mailinglist.txt` contains emails adresses, one per line, for everyone 
who should receive an email every weekday with the complete lunch menu.

## Contribute
You can contribue by writing a lunch restaurant module if you feel there is one
missing.  Some key functionality is still missing:

  * Automatically create a poll
  * Send emails to everyone

Below follows some suggestions for areas that can be improved.

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



### Doodle API
It would be cool to implement automatic Doodle poll generation.
Doodle has a Poll Wizard API that might be used to generate polls:

http://doodle.com/wizard/DoodleWizard.pdf
