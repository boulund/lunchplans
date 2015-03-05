#!/usr/bin/env python2.7
# coding: utf-8
# Authors:
#  Fredrik Boulund
# Purpose:
#  Generate daily lunch menu summaries 

from sys import argv, exit
from email.mime.text import MIMEText
import logging
import smtplib
import requests

from restaurants import restaurants

logger = logging.getLogger("lunchplans")

def get_lunch_menus():
    """ Get lunch menus from all restauraunts.
    """
    menus = {}
    for restaurant in restaurants:
        menu = restaurant.todays_lunch()
        if type(menu) is str:
            menu = menu.decode("utf-8")
        menus[restaurant.name] = menu
    return menus


def create_combined_menu(menus):
    """ Combine all menus into one single string.
    """
    supermenu = []
    for rest, menu in restaurant_menus.iteritems():
        supermenu.append(rest.decode("utf-8").center(40, "-"))
        supermenu.append(menu)
        supermenu.append("")
    return "\n".join(supermenu)


def parse_mailinglist(filename):
    """ Parse mailinglist.
    """
    emails = []
    with open(filename) as f:
        for line in f:
            emails.append(line.strip())
    if len(emails) < 1:
        logger.info("Found no email addresses in mailinglist.txt")
    return emails


def send_emails(message, mailinglist, sender="lunchbot@mailinator.com"):
    """ Send emails with message to all recipients.
    """
    recipients = parse_mailinglist(mailinglist)
    s = smtplib.SMTP("localhost")
    msg = MIMEText(message, _charset="UTF-8")
    msg["Subject"] = "Lunchplans?"
    msg["From"] = sender
    msg["To"] = ",".join(recipients)
    s.sendmail(sender, "fredrik.boulund@chalmers.se", msg.as_string())


if __name__ == "__main__":
    restaurant_menus = get_lunch_menus()
    supermenu = create_combined_menu(restaurant_menus)
    send_emails(supermenu, "mailinglist.txt")
