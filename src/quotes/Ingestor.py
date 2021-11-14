from typing import List

from quotes import (
    IngestorInterface,
    CSVIngestor,
    DocxIngestor,
    PDFIngestor,
    TextIngestor,
)


class Ingestor(IngestorInterface):
    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[DocxIngestor]:
        for ingestor in cls.Ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
