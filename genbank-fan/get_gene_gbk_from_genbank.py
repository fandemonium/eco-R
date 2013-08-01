from Bio import Entrez
import sys

l = []
with open (sys.argv[1]) as f:
    next(f)
    for line in f:
        lexemes = line.split('\t')
        id = lexemes[-6]
        l.append(id.rstrip())
print l

for each in l:
    Entrez.email = "fyang@iastate.edu"
    handle = Entrez.efetch(db="nucleotide", id=each, rettype="gb", retmode="text")
    fp = open(each + '.gbk', 'w')
    fp.write('%s' % handle.read())
