# coding: utf-8
# Module: Time Out Bistro
# Authors:
#  Fredrik Boulund

from datetime import datetime
from bs4 import BeautifulSoup as bs
import logging
import requests

name = "Time Out Bistro"

def todays_lunch():
    """ Retrieve today's lunch menu from Time Out Bistro.
    """
    today = datetime.now().date()
    weekdays = {0: "Måndag", 1: "Tisdag", 2: "Onsdag", 3: "Torsdag",
                4: "Fredag", 5: "Lördag", 6: "Söndag"}
    weekday = weekdays[datetime.now().weekday()]

    logging.debug("Downloading the RSS for Time Out Bistro from their facebook page on {}".format(today))
    rss = "https://www.facebook.com/feeds/page.php?format=rss20&id=135890329899423"
    rss_xml = requests.get(rss)
    soup = bs(rss_xml.text)
    
    menu_items = []
    for item in soup.find_all("item"):
        desc = item.description.string.split("<br")
        day = desc[0]
        if weekday in day.split()[0]:
            regular = desc[3].strip(" <>/")
            veg = desc[6].strip(" <>/")
            logging.debug("Found menu for {}".format(day))
            menu_items.append(regular)
            menu_items.append(veg)
            break
    else:
        menu_items.append("Error parsing menu")
    menu = "\n".join(menu_items)

    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

