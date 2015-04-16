#!/usr/bin/env python2.7
# coding: utf-8
# Authors:
#  Fredrik Boulund
# Purpose:
#  Generate daily lunch menu summaries 

from sys import argv, exit
from email.mime.text import MIMEText
import argparse
import logging
import smtplib
import requests

from restaurants import restaurants


def parse_commandline(argv):
    """ Parse commandline arguments.
    
    Input: argv
    Returns:  options, logger
    """
    
    desc = """Lunchplans -- summarize lunch restaurant options."""
    parser = argparse.ArgumentParser(description=desc)
    
    parser.add_argument("-e", "--email", dest="email",
                        default="",
                        help="Email address to send summary to. A filename with one email address per line can be specified instead [default: not used].")
    parser.add_argument("--email-server", dest="email_server",
                        default="localhost",
                        help="Specify email server [default: %(default)s].")
    parser.add_argument("--email-port", dest="email_port",
                        type=int,
                        default=25,
                        help="Port to send email on [default: %(default)s].")
    parser.add_argument("--sender-email", dest="sender_email",
                        default="lunchbot@mailinator.com",
                        help="Specify sender email address [default: %(default)s]")
    
    devopts = parser.add_argument_group("Developer options", "Use at your own peril!")
    devopts.add_argument("--loglevel",
                         choices=["DEBUG", "INFO"],
                         default="INFO",
                         help="Set logging level [default: %(default)s].")
    
    options = parser.parse_args()
    
    # Setup logging
    logger = logging.getLogger("lunchplans")
    logger.addHandler(logging.StreamHandler())
    if options.loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    
    return options, logger
    
    

def get_lunch_menus():
    """ Get lunch menus from all restauraunts.
    """
    menus = {}
    for restaurant in restaurants:
        menu = restaurant.todays_lunch()
        if isinstace(menu, str):
            menu = menu.decode("utf-8")
        menus[restaurant.name] = menu
    logger.debug("Finished parsing restaurant menus.")
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


def send_emails(message, target, sender, server, port):
    """ Send emails with message to all recipients.
    """
    if "@" in target:
        recipients = [target]
    else:
        recipients = parse_mailinglist(mailinglist)
        
    logger.debug("Sending email(s) to: {}".format(recipients))
    s = smtplib.SMTP(server, port=port)
    msg = MIMEText(message, _charset="UTF-8")
    msg["Subject"] = "Lunchplans?"
    msg["From"] = sender
    msg["To"] = ",".join(recipients)
    s.sendmail(sender, recipients[0], msg.as_string())
    logger.debug("Email(s) sent.")



if __name__ == "__main__":
    options, logger = parse_commandline(argv)
    restaurant_menus = get_lunch_menus()
    supermenu = create_combined_menu(restaurant_menus)
    print supermenu
    
    if options.email:
        send_emails(supermenu,
                    target=options.email,
                    sender=options.sender_email,
                    server=options.email_server,
                    port=options.email_port)
