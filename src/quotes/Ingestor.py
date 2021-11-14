#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE:
#
##

from typing import List

from .quote_model import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Check for the type of the document and parse the document with
    the correct ingestor.
    """

    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse any kind of document that can be handeled
        with one of the Ingestors.

        Args:
            path (str): path to the document to be ingested.

        Returns:
            List[QuoteModel]: list of QuoteModel objects.
        """
        for ingestor in cls.Ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
