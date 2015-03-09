# coding: utf-8
# Module: Time Out Bistro
# Authors:
#  Fredrik Boulund
#  Tobias Abenius

from datetime import datetime
import xml.etree.cElementTree as xet
import logging
import requests

name = "Time Out Bistro"

def todays_lunch():
    """ Retrieve today's lunch menu from Time Out Bistro.
    """
    today = datetime.now().date()
    weekdays = {0: u"Måndag", 1: u"Tisdag", 2: u"Onsdag", 3: u"Torsdag",
                4: u"Fredag", 5: u"Lördag", 6: u"Söndag"}
    weekday = weekdays[datetime.now().weekday()]

    logging.debug(u"Downloading the RSS for Time Out Bistro from their facebook page on {}".format(today))
    rss = "https://www.facebook.com/feeds/page.php?format=rss20&id=135890329899423"
    rss_xml = requests.get(rss)
    tree = xet.fromstring(rss_xml.text.encode('utf-8'))
    chan = tree.getchildren()[0]
    
    menu_items = []
    for item in chan.findall("item"):
        desc = item.find('description').text
	desc = [a.replace("/>","").replace(">","").strip() for a in desc.split("<br") ]
	desc = filter(lambda e: e!="" and e!="br", desc)
	day = desc[0].split()[0]
	if weekday in day:
	    if desc[1].lower().startswith("dagens"):
              meat = desc[2].strip(" <>/")
       	    if desc[3].lower().startswith("veg"):
              veg = desc[4].strip(" <>/")
            logging.debug(u"Found menu for {}".format(day))
            menu_items.append(meat)
            menu_items.append(veg)
            break
    else:
        menu_items.append(u"Error parsing menu")
    menu = u"\n".join(menu_items)

    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

