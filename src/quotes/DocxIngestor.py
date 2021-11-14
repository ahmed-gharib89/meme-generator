#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: DocxIngestor class
#
##

from typing import List
import docx

from quotes import QuoteModel, IngestorInterface, CannotIngestException


class DocxIngestor(IngestorInterface):
    """Import a docx file into a Qoute object ."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a docx file containing the Qoutes.

        Args:
            path (str): path to the document to be ingested.

        Raises:
            Exception: if the document is not a docx file.

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
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(" - ")
                new_qoute = QuoteModel(parse[0], parse[1])
                qoutes.append(new_qoute)

        return qoutes
