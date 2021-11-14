#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: PDFIngestor class
#
##
from typing import List

from .IngestorInterface import IngestorInterface
from .QouteModel import QouteModel
from .utility import CannotIngestException, parse_text


class TextIngestor(IngestorInterface):
    """Import a text file into a Qoute object ."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QouteModel]:
        """Parse a text file containing the Qoutes.

        Args:
            path (str): path to the document to be ingested.

        Raises:
            Exception: if the document is not a text file.

        Returns:
            List[QouteModel]: list of QouteModel objects.
        """
        if not cls.can_ingest(path):
            msg = (
                f"file: {path}"
                "the extension of the file is not in the allowed extension"
                f"allowed extensions: [{cls.allowed_extensions}]"
            )
            raise CannotIngestException(msg)

        qoutes = parse_text(path)

        return qoutes
