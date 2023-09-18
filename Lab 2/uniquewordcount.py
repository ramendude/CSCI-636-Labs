from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class UniqueWordCount(MRJob):

    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for word in words:
            yield word,1

    def reducer(self,word,count):
        yield word,1

if __name__ == '__main__':
     UniqueWordCount.run()

