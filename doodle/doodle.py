# coding: utf-8
# Module: Doodle
# Authors:
#  Fredrik Boulund

import requests

def generate_doodle(restaurant_menus):
    """ Generate a Doodle poll with all the lunch restaurants as options.
    Put the available menus in the description.
    """

    # Creates a Doodle poll with :
    # Text poll: type=text
    # Ifneedbe poll: levels=3
    # Language English: locale=en
    # Title: title=Lunchplans
    # User: name=Lunchbot
    # Options (<one per lunch restaurant module available>): optionN=<restaurantname>
    # Description: <Menu strings from each restaurant>

    payload = {"type": "text",
            "levels": "3",
            "locale": "en",
            "title": "Lunchplans",
            "name": "Lunchbot",
            "eMailAdress": "fredrik.boulund@chalmers.se"}
    menus = []
    for num, restaurant_menu in enumerate(restaurant_menus.iteritems()):
        option = "option{}".format(num+1)
        restaurant, menu = restaurant_menu
        payload[option] = restaurant
        menus.append(menu)
    description = "\n".join(menus)
    payload["description"] = description

    # TODO: This doesn't work. Probably going to need something better
    # It seems Doodle's REST API is no more...
    doodle_request = "http://doodle.com/polls/wizard.html"
    r = requests.get(doodle_request, params=payload)
    print r.url

    return
