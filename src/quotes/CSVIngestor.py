#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: CSVIngestor class
#
##
import pandas as pd
from typing import List

from .quote_model import QuoteModel
from .IngestorInterface import IngestorInterface
from .utility import CannotIngestException, parse_text


class CSVIngestor(IngestorInterface):
    """Import a csv file into a Qoute object ."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a csv file containing the Qoutes.

        Args:
            path (str): path to the document to be ingested.

        Raises:
            Exception: if the document is not a csv file.

        Returns:
            List[QuoteModel]: list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            msg = (
                f"file: {path}"
                "the extension of the file is not in the allowed extension"
                f"allowed extensions: [{cls.allowed_extensions}]"
            )
            raise CannotIngestException(msg)

        qoutes = []
        df = pd.read_csv(path, header=0, encoding="utf-8")

        for row in df.itertuples():
            new_qoute = QuoteModel(row.body, row.author)
            qoutes.append(new_qoute)

        return qoutes
