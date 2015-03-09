# coding: utf-8
# Module: Nära Hem Catering: Chalmersvillan
# Authors:
#  Fredrik Boulund

from datetime import datetime
from bs4 import BeautifulSoup as bs
import logging
import requests

name = "Chalmersvillan"

def todays_lunch():
    """ Retrieve today's lunch options from Chalmersvillan Gibraltargatan 1A.
    """
    today = datetime.now().date()
    weekdays = {0: u"Måndag", 1: u"Tisdag", 2: u"Onsdag", 3: u"Torsdag",
                4: u"Fredag", 5: u"Lördag", 6: u"Söndag"}
    weekday = weekdays[datetime.now().weekday()]

    logging.debug(u"Downloading the menu for Chalmersvillan on {}, {}".format(today, weekday))
    webpage = "http://narahem-catering.blogspot.se/p/matsedel-villan.html"
    r = requests.get(webpage)

    soup = bs(r.text)
    text = soup.get_text().split("\n")
    menu_items = []
    for idx, item in enumerate(text):
        if weekday in item:
            menu_items.append(text[idx+2])
            menu_items.append(text[idx+4])
            break
    else:
        menu_items.append(u"Error parsing menu")

    menu = "\n".join(menu_items)
    return menu



if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

