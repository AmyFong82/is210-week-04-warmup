#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function checking if required and optional defaults are the same."""


def defaults(my_required, my_optional=True):
    """Check to see if my_required and my_optional arguments are the same.

    Args:
        my_required (bool): Either True or False.
        my_optional (bool, optional): Either True or False. Default: True.

    Returns:
        bool: If my_required is the same object as my_optional, return True.
              If not, return False.

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
