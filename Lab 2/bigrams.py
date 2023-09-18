from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class bigrams(MRJob):
    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            c = a + "," + b
            yield c,1

    def reducer(self,word,count):
        total_count = sum(count)
        yield word, total_count

if __name__ == '__main__':
    bigrams.run()