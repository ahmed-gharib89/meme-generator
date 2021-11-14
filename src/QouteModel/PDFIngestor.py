#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: PDFIngestor class
#
##
import subprocess
import os
import random
from typing import List

from .IngestorInterface import IngestorInterface
from .QouteModel import QouteModel
from .utility import CannotIngestException, parse_text


class PDFIngestor(IngestorInterface):
    """Import a pdf file into a Qoute object ."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QouteModel]:
        """Parse a pdf file containing the Qoutes.

        Args:
            path (str): path to the document to be ingested.

        Raises:
            Exception: if the document is not a pdf file.

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
        tmp = f"./tmp/{random.randint(0,100000000)}.txt"
        call = subprocess.call(["pdftotext", path, tmp])

        qoutes = parse_text(tmp)
        os.remove(tmp)

        return qoutes
