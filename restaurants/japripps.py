# coding: utf-8
# Module: J.A. Pripps
# Authors:
#  Fredrik Boulund
#  Tobias Abenius

from datetime import datetime
import xml.etree.cElementTree as xet
import logging
import requests

name = "J.A. Pripps pub"

def todays_lunch():
    """ Retrieve today's lunch menu from J.A. Pripps.
    """
    today = datetime.now().date()
    weekdays = {0: u"m\xe5ndag", 1: u"tisdag", 2: u"onsdag", 3: u"torsdag",
                4: u"fredag", 5: u"lördag", 6: u"söndag"} 
    weekday = weekdays[datetime.now().weekday()]

    logging.debug(u"Downloading the RSS for J.A. Pripps from their facebook page on {}".format(today))
    rss = "https://www.facebook.com/feeds/page.php?format=rss20&id=188556421182822"
    rss_xml = requests.get(rss)
    tree = xet.fromstring(rss_xml.text.encode('utf-8'))
    chan = tree.getchildren()[0]
    
    menu_items = []
    for item in chan.findall("item"):
        desc = item.find('description').text
	desc = [a.replace("/>","").replace(">","").strip() for a in desc.split("<br") ]
	desc = filter(lambda e: e!="" and e!="br", desc)
	day = desc[0].split()[1].rstrip('!')
	if weekday in day:
 	   logging.debug(u"Found menu for {}".format(day))
 	   menu_items.append(u"\n".join(desc[1:-1]))
 	   break
	else:
	    menu_items.append(u"Error parsing menu")
    menu = u"\n".join(menu_items)

    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

