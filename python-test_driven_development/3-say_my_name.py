#!/usr/bin/python3
"""
This module contains the function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints, "My name is <first_name> <last_name>".
    If last_name is not provided, only first_name will print.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
