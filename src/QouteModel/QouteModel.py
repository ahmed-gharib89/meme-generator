#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: class for the QouteModel
#
##


class QouteModel:
    """
    This class is for the QouteModel
    """

    def __init__(self, quote: str, author: str) -> None:
        """
        This function is the constructor of the QouteModel class
        """
        self.quote = quote
        self.author = author

    def __str__(self) -> str:
        """The string representation of QouteModel .

        Returns:
            str: Human readable string representation of QouteModel.
        """
        return f"{self.quote} - {self.author}"

    def __repr__(self) -> str:
        """Return a string representation of the Qoute model .

        Returns:
            str: Machine readable string representation of QouteModel.
        """
        return f"QouteModel({self.quote}, {self.author})"
