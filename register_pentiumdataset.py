import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries
from typing import NamedTuple
from ir_datasets.datasets.base import Dataset

class IrAnthologyDocument(NamedTuple):
    doc_id: str
    abstract: str
    editors: list
    authors: list
    year: str
    booktitle: str
    publisher: str

    def default_text(self):
        return self.booktitle + ' ' + self.abstract + ' ' + self.authors + ' ' + self.publisher

ir_datasets.registry.register('iranthology-pentium', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='iranthology-pentium/ir-anthology-processed.jsonl'), doc_cls=IrAnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='iranthology-pentium/topics.xml'), lang='en')
))
