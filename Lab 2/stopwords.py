from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class WordCountStopWords(MRJob):
    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for word in words:
            yield word,1

    def reducer(self,word,count):
        filter = ['the','and','of','a','to','in','is','it']
        if word.lower() not in filter:
            yield word,1

if __name__ == '__main__':
    WordCountStopWords.run()