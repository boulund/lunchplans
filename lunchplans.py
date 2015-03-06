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
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
debugmode = True

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


def create_combined_menu(restaurant_menus):
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

def get_smtp_server():
    """ Get the SMTP server host, port
    """
    filename = "smtpserver.txt"
    server = "localhost"
    port = 25
    try:
	serverport = open(filename).readline().split(':')
	server = serverport[0]
	if (len(serverport) > 1):
	    port = int(serverport[1])
    except IOError:
        logger.info("file '%s' not found, using default smtp server %s:%d" %(filename,server,port))
    return dict(server=server, port=port)

def send_emails(message, mailinglist, sender="lunchbot@mailinator.com"):
    """ Send emails with message to all recipients.
    """
    recipients = parse_mailinglist(mailinglist)
    server = get_smtp_server()
    if debugmode:
        print message
    else:
	s = smtplib.SMTP(server['server'],port=server['port'])
	msg = MIMEText(message, _charset="UTF-8")
	msg["Subject"] = "Lunchplans?"
	msg["From"] = sender
	msg["To"] = ",".join(recipients)
        s.sendmail(sender, "fredrik.boulund@chalmers.se", msg.as_string())

if __name__ == "__main__":
    restaurant_menus = get_lunch_menus()
    supermenu = create_combined_menu(restaurant_menus)
    send_emails(supermenu, "mailinglist.txt")
