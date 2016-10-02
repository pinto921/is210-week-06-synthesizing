#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" string with inputs"""

def prepare_email(appointments):
    """ takes a string and formats with given inputs

    Args:
        appointments (lists): name and date tuple

    Returns:
        email (str): format_string with given inputs

    Example:
        >>> prepare_email(['Jen", '2015'), ('max', 'march 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max, \ nI look forward to meeting you on March 3.\nBest\nMe']

    """

    format_string = 'Dear {}, \nI look forward to meeting you {}. \nBest, \nMe'
## tuple_counter =0
## list_counter = 0
    for obj in appointments:
## tuple_counter += 1
## list_counter += 1
## return email
