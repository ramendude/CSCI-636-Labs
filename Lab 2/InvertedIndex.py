from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class InvertedIndex(MRJob):
    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        match = re.search(r'Document (\d+): (.+)', line)
        doc= match.group(1)
        for word in words:
            yield word, "Document " + doc
    def reducer(self,word,doc):
        total_doc = list(doc)
        filter = ['document','1','2','3',':']
        if word.lower() not in filter:
            yield word, total_doc

if __name__ == '__main__':
    InvertedIndex.run()