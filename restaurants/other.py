# coding: utf-8
# Module: Other restaurants
# Authors:
#  Fredrik Boulund
# Description:
#  This module is meant to give restaurants
# that do not have an online meny a representation
# in the lunchplans.py output.
#  Add suggestions to other.txt.


name = "Other"

def todays_lunch():
    """ Return a list of placeholder menus for restaurants lacking an online menu.
    """
    
    menu_items = []
    with open("other.txt") as f: 
        for line in f:
            menu_items.append(line.strip())
    menu = "\n".join(menu_items)
    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()
