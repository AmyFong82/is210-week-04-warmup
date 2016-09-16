#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """returns a string with winks and nudges.

    Args:
        wink (str): A string to be repeated by the number assigned to numwink.
        numwink (int, optional): The number of times wink and nudge will be
                                 repeated. Default: 2

    Returns:
        str: Concatenate winks and nudges for number of times assigned
             to numwink to the end of the string.

    Examples:

        >>> know_what_i_mean('wink ')
        'Know what I mean? wink wink, nudge nudge'

        >>> know_what_i_mean('wink ', 1)
        'Know what I mean? wink, nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
