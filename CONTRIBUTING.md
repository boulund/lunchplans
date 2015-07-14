# Contributing
Several things can be contributed by you:

  * Add more restaurant modules (lunch menu parsers/scrapers)
  * "Lunchbot"-code that suggests a lunchplace each day.
	 Can be expanded with lots of ideas; Markov chain-based etc.

If you expect your contribution to require involvment of more people than just
yourself, please keep development of your new feature in a separate branch. It
is very easy to separate development into a separate branch:

    hg branch my-new-feature
	<do whatever you want; create files, folders>
	hg add <all new files>
	hg commit -m "Added feature XYZ"
	hg pull -u
	hg push

Everything you do in the repository after creating a new branch will belong to
that branch.  To switch back to the *default* branch (or any other branch) is
also easy:

    hg update other-branch
	<development work on other-branch>
	hg commit -m "Modified how dates for restaurant XYZ are parsed"
    hg pull -u
	hg push

This changes to *other-branch* and prepares your directory to work on that
branch. When development of your new feature is completed and fully tested, the
branch can be merged back into the *default* branch, like so:

	hg pull -u
    hg update default
	hg merge my-new-feature
	hg push


## TODO
First off, please review any open
[Issues](https://bitbucket.org/chalmersmathbioinformatics/lunchplans/issues?status=new&status=openhttps://bitbucket.org/chalmersmathbioinformatics/lunchplans/issues?status=new&status=open)
for the project and see if you can fix any of those. In addition, we keep a
brief TODO-list in this file with ideas for future improvements.
Here is a list of suggested TODOs for the project

### TODO-list

  * Add restaurant module for *restaurant*
  * Create a lunchbot module that makes automatic suggestions
  * *Your idea*


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

The development of Doodle-related stuff is currently located in the **doodle**
branch of the repository. Please keep all Doodle-related development in that
branch.

