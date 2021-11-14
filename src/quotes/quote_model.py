#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: class for the QuoteModel
#
##


class QuoteModel:
    """
    This class is for the QuoteModel
    """

    def __init__(self, body: str, author: str) -> None:
        """
        This function is the constructor of the QuoteModel class
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """The string representation of QuoteModel .

        Returns:
            str: Human readable string representation of QuoteModel.
        """
        return f"{self.body} - {self.author}"

    def __repr__(self) -> str:
        """Return a string representation of the Qoute model .

        Returns:
            str: Machine readable string representation of QuoteModel.
        """
        return f"QuoteModel({self.body}, {self.author})"
