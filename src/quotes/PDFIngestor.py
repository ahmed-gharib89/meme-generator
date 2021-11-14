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

from .quote_model import QuoteModel
from .IngestorInterface import IngestorInterface
from .utility import CannotIngestException, parse_text


class PDFIngestor(IngestorInterface):
    """Import a pdf file into a Qoute object ."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a pdf file containing the Qoutes.

        Args:
            path (str): path to the document to be ingested.

        Raises:
            Exception: if the document is not a pdf file.

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

        tmp_dir = os.path.join(os.getcwd(), "tmp")
        tmp = os.path.join(tmp_dir, f"{random.randint(0,100000000)}.txt")
        os.makedirs(tmp_dir, exist_ok=True)
        print(tmp_dir)
        print(tmp)
        print(path)

        subprocess.run(
            ("pdftotext", "-layout", "-nopgbrk", path, tmp), check=True
        )

        qoutes = parse_text(tmp)
        os.remove(tmp)

        return qoutes
