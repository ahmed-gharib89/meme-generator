#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: Abstract class for the ingestors
#
##

from abc import ABC, abstractmethod

from typing import List
from quotes import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return whether the document type can be ingested .

        Args:
            path (str): path to the document to be ingested.

        Returns:
            bool: True if the extension is allowed, False otherwise.
        """
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse documents."""
        pass
