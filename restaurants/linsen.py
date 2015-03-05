# coding: utf-8
# Module: Linsen Chalmers Johanneberg
# Authors:
#  Fredrik Boulund

from datetime import datetime
from bs4 import BeautifulSoup as bs
import logging
import requests

name = "Linsen"

def todays_lunch():
    """ Retrieve today's lunch options from Linsen Johanneberg.
    """

    today = datetime.now().date()

    logging.debug("Downloading the RSS for Linsen on {}".format(today))
    rss = "http://cm.lskitchen.se/johanneberg/linsen/sv/{}.rss".format(today)
    rss_xml = requests.get(rss)
    soup = bs(rss_xml.text)
    
    menu_items = []
    for item in soup.find_all("item"):
        menu_items.append(item.title.string)
        if "@" in item.description.string:
            menu_items.append(item.description.string.split("@")[0])
        else:
            menu_items.append(item.description.string)
    menu = "\n".join(menu_items)

    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()
