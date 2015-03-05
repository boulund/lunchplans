# coding: utf-8
# Module: Restaurang Einstein
# Authors:
#  Fredrik Boulund

from datetime import datetime
from bs4 import BeautifulSoup as bs
import logging
import requests

name = "Einstein"

def todays_lunch():
    """ Retrieve today's lunch menu from Restaurang Einstein.
    """
    today = datetime.now().date()
    weekdays = {0: "Måndag", 1: "Tisdag", 2: "Onsdag", 3: "Torsdag",
                4: "Fredag", 5: "Lördag", 6: "Söndag"}
    weekday = weekdays[datetime.now().weekday()]

    logging.debug("Downloading the menu for Einstein on {}, {}".format(today, weekday))
    webpage = "http://butlercatering.se/print/6"
    r = requests.get(webpage)

    soup = bs(r.text)
    text = soup.get_text().split("\n")
    menu_items = []
    for idx, item in enumerate(text):
        if weekday in item:
            menu_items.append(text[idx+1])
            menu_items.append(text[idx+2])
            break
    else:
        menu_items.append("Error parsing menu")
    menu = "\n".join(menu_items)
    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

