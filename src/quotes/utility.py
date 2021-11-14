#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: helper functions and classes for the QuoteModel
#
##
from typing import List
from .quote_model import QuoteModel


class CannotIngestException(Exception):
    """Exception to be raised when a document cannot be ingested."""

    pass


def parse_text(fpath: str) -> List[QuoteModel]:
    """Parse a text file and return a list of Qoute instances .

    Args:
        fpath (str): file path to the text file to be parsed.

    Returns:
        List[QuoteModel]: a list of QuoteModel instances.
    """
    file_ref = open(fpath, "r")
    qoutes = []

    for line in file_ref.readlines():
        line = line.strip("\n\r").strip()
        if len(line) > 0:
            parse = line.split(" - ")
            new_qoute = QuoteModel(parse[0], parse[1])
            qoutes.append(new_qoute)

    file_ref.close()
    return qoutes
