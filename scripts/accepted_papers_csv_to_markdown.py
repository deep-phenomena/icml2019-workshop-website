import csv
from dataclasses import dataclass
import sys
from typing import List

@dataclass
class Paper:
    title: str
    authors: List[str]
    decision: str
    url: str

assert len(sys.argv) == 2

filename = sys.argv[1]

papers = []

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        papers.append(Paper(title=row[2], authors=row[1].split(', '), url=row[3], decision=row[0]))

for p in papers:
    if p.decision != 'Accept':
        continue
    print(f'- [{p.title}]({p.url})')
    if len(p.authors) == 1:
        author_string = p.authors[0]
    elif len(p.authors) == 2:
        author_string = p.authors[0] + ' and ' + p.authors[1]
    else:
        author_string = ', '.join(p.authors[:-1])
        author_string += ', and ' + p.authors[-1]
    print(f'*{author_string}*')
