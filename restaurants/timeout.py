# coding: utf-8
# Module: Time Out Bistro
# Authors:
#  Fredrik Boulund
#  Tobias Abenius

from datetime import datetime
#from bs4 import BeautifulSoup as bs
import xml.etree.cElementTree as xet
import logging
import requests
import pdb

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
#    soup = bs(rss_xml.text)
    tree = xet.fromstring(rss_xml.text.encode('utf-8'))
    chan = tree.getchildren()[0]
    
    menu_items = []
    for item in chan.findall("item"):
#	pdb.set_trace()
        desc = item.find('description').text
        #desc = u"".join(unicode(a) for a in item.description.contents).split(u"<br")
        #desc = [unicode(a) for a in desc]
        #desc = [a.strip(u" <>/") for a in desc]
	desc = [a.replace("/>","").replace(">","").strip() for a in desc.split("<br") ]
	desc = filter(lambda e: e!="" and e!="br", desc)
	day = desc[0].split()[0]
        #desc = item.description.split("<br")
        #day = desc[0]
	if weekday in day:
	    if desc[1].lower().startswith("dagens"):
              meat = desc[2].strip(" <>/")
       	    if desc[3].lower().startswith("veg"):
              veg = desc[4].strip(" <>/")
            logging.debug("Found menu for {}".format(day))
            menu_items.append(meat)
            menu_items.append(veg)
            break
    else:
        menu_items.append("Error parsing menu")
    menu = "\n".join(menu_items)

    return menu


if __name__ == "__main__":
    print name.center(40, "-")
    print todays_lunch()

