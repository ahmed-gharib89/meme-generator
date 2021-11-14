from typing import List

from .IngestorInterface import IngestorInterface
from .QouteModel import QouteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[DocxIngestor]:
        for Ingestor in cls.Ingestors:
            if Ingestor.can_ingest(path):
                return Ingestor.parse(path)
