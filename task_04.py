#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function checking if there are too many kittens."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Test if there are too many kittens.

    Args:
        kittens (int): the number of kittens
        litterboxes (int): the number of available litterboxes
        catfood (bool): whether or not any catfood exists

    Returns:
        bool: if the number of kittens is bigger than the number of litterboxes
              or there is no catfood available, return True. Else return false.

    Examples:
        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
