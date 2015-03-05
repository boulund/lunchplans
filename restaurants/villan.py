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
    weekdays = {0: "Måndag", 1: "Tisdag", 2: "Onsdag", 3: "Torsdag",
                4: "Fredag", 5: "Lördag", 6: "Söndag"}
    weekday = weekdays[datetime.now().weekday()]

    logging.debug("Downloading the menu for Chalmersvillan on {}, {}".format(today, weekday))
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
        menu_items.append("Error parsing menu")

    menu = "\n".join(menu_items)
    return menu



if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

